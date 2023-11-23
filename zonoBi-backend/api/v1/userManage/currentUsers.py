# -*- encoding: utf-8 -*-
'''
@Date		:2023/11/23 17:27:41
@Author		:zono
@Description:当前用户接口
'''
from datetime import datetime, timedelta
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status


# ---------------------数据库有关的导入------------------------------------------
from sqlalchemy.orm import Session

from database.sqlite import engine, Base, SessionLocal

from crud import crud
from models import base
from schemas import schemas

# ----------------------------有关安全的导入-----------------------------------
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

currentUsers = APIRouter(tags=["用户管理"])

Base.metadata.create_all(bind=engine)

# TODO 加入配置文件中------------------------初始化设置---------------------------------------
SECRET_KEY = "efb8d310a2e46e859a8e2f196ad25ff41916c90828999d64d50699f4f6cae93c"  # TODO 加入配置中
ALGORITHM = "HS256"  # 算法变量
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 过期时间


pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto")  # 使用bcrypt算法对密码加密
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login/account")  # 用户校验地址
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


async def get_current_users(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    @description  :
    校验Token，验证用户，并获取用户信息
    @param  :
    -------
    @Returns  :
    -------
    """
    # TODO 获取用户量可以设置
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="您无权访问",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = jwt.decode(token, SECRET_KEY, algorithms=[
        ALGORITHM])  # 与encode反过来
    username: str = payload.get("sub")
    token_data = crud.get_user_by_username(db, username)
    if token_data.userRole:  # true为管理员
        token_data = crud.get_users(db, skip=0, limit=100)
    else:
        raise credentials_exception
    return token_data

# ---------------------------------------------------------------


async def get_current_users(current_users=Depends(get_current_users)):
    """
    @description  :
    对获取的数据进行判断
    1.是否为活跃用户
    2.是否为管理员
    @param  :
    -------
    @Returns  :
    -------
    """
    for user in current_users:
        del user.__dict__['userPassword']  # 删除密码
    return current_users


@currentUsers.get("/currentUsers")
async def read_users_me(current_users=Depends(get_current_users)):
    """
    @description  :
    获取多名用户信息
    @param  :
    -------
    @Returns  :
    -------
    """
    return current_users
