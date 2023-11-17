# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/06 15:50:36
@Author		:zono
@Description:注册接口，把密码哈希
'''
from fastapi import APIRouter, Depends, HTTPException

from passlib.context import CryptContext

from sqlalchemy.orm import Session

from database.sqlite import engine,Base,SessionLocal
from crud import crud
from schemas import schemas



reg = APIRouter()

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")#使用bcrypt算法对密码加密

# Dependency
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

def get_password_hash(password: str):
    """
    @description  :
    对密码加密
    @param  :
    -------
    @Returns  :
    str
    """
    return pwd_context.hash(password)

@reg.post("/reg/", response_model=schemas.User, summary="注册接口")
async def registration(user: schemas.UserInDB, db: Session = Depends(get_db)):
    """
    @description  :
    注册接口，对传入的账号密码进行注册，并把数据加入数据库，密码哈希一次
    @param  :
    username:学号
    password:密码
    @Returns  :
    -------
    """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="该用户名已经被使用")
    user.password = get_password_hash(user.password)
    crud.create_user(db=db, user=user)
    raise HTTPException(status_code=200, detail="成功创建用户")
