# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/06 18:02:04
@Author		:zono
@Description:登录接口
'''
from datetime import datetime, timedelta
from typing import Union

from fastapi import APIRouter, Depends, HTTPException,status


# ---------------------数据库有关的导入------------------------------------------
from sqlalchemy.orm import Session

from database.sqlite import engine,Base,SessionLocal

from crud import crud
from models import base
from schemas import schemas

# ----------------------------有关安全的导入-----------------------------------
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

loginUP = APIRouter()

Base.metadata.create_all(bind=engine)

# ------------------------初始化设置---------------------------------------
SECRET_KEY = "efb8d310a2e46e859a8e2f196ad25ff41916c90828999d64d50699f4f6cae93c"#TODO 加入配置中
ALGORITHM = "HS256"#算法变量
ACCESS_TOKEN_EXPIRE_MINUTES = 30#过期时间


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")#使用bcrypt算法对密码加密
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")#用户校验地址


# ---------------------------------------------------------------

# 数据库的打开和关闭
def get_db():
    """
    @description  :
    底层依赖，每个接口都会调用该函数，打开会话，然后关闭会话，由depends导入
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------函数区----------------------------------------
def verify_password(plain_password:str, hashed_password:str) -> bool:
    """
    @description  :
    校验密码
    @param  :
    -------
    @Returns  :
    bool
    """
    return pwd_context.verify(plain_password, hashed_password)
    
def authenticate_user(username: str, password: str,db):
    """
    @description  :
    调用数据库对数据进行比对
    @param  :
    -------
    @Returns  :
    -------
    """
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    db_user=db.query(base.User).filter(base.User.username== username).first()
    if not verify_password(password, db_user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    @description  :
    创建Token函数
    @param  :
    -------
    @Returns  :
    -------
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta#加上过期时间
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)#TODO默认过期时间，集成到config中
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)#入值：字符、key、算法->出值：Token
    return encoded_jwt

# --------------------------接口调用-------------------------------------
@loginUP.post("/token",response_model=schemas.Token,summary="获取Token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    """
    @description  :
    登录接口,并返回Token
    @param  :
    -------
    @Returns  :
    access_token
    """
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="账号或密码错误，或该用户不存在",
                             headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# -----------------------------调用接口取信息----------------------------------


async def get_current_user(db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    """
    @description  :
    校验Token，验证用户，并获取当前用户
    @param  :
    -------
    @Returns  :
    -------
    """
    #TODO 获取用户量可以设置,调整对应用户才能使用对应数据
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据，可能是登录过期,或者用户已注销",#TODO 日后完善
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])#与encode反过来
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        #XXX获取所有用户 token_data = crud.get_users(db, skip=0, limit=100)
        token_data = crud.get_user_by_username(db, username)
        #TODO修改为只取对应用户
    except JWTError:
        raise credentials_exception
    return token_data

#TODO post应该也有办法
# ---------------------------------------------------------------
async def get_current_active_user(current_user: schemas.UserInDB = Depends(get_current_user)):
    """
    @description  :
    检验用户权限
    @param  :
    -------
    @Returns  :
    -------
    """
    return current_user

@loginUP.get("/users/me")
async def read_users_me(current_user: schemas.UserInDB = Depends(get_current_active_user)):
    """
    @description  :
    一般用户
    @param  :
    -------
    @Returns  :
    -------
    """
    return current_user
