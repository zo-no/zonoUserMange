# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/07 16:26:03
@Author		:zono
@Description:输出文章列表、输出文章内容
'''
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from database.sqlite import engine, Base, SessionLocal

from crud import crud
from models import base
from schemas import schemas

articleOutput = APIRouter()

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


@articleOutput.get("/channels", status_code=200, summary="文章频道")
async def channelsOutput():
    """
    @description  :
    返回频道分类
    @param  :
    -------
    @Returns  :
    -------
    """
    return {
        "channels": [
            {"id": 1, "name": "Python"},
            {"id": 2, "name": "Java"},
            {"id": 3, "name": "C++"},
            {"id": 4, "name": "C"},
            {"id": 5, "name": "Go"},
            {"id": 6, "name": "PHP"},
            {"id": 7, "name": "JavaScript"}
        ]}

# TODO artcleOutput


async def get_current_article(db: Session = Depends(get_db)):
    """
    @description  :
    检验用户权限
    @param  :
    -------
    @Returns  :
    -------
    """
    current = crud.get_article(db)
    return current


@articleOutput.get("/articles", status_code=200, summary="文章获取")
async def read_users_me(current: schemas.UserInDB = Depends(get_current_article)):
    """
    @description  :
    一般用户
    @param  :
    -------
    @Returns  :
    -------
    """
    # zono = get_current_active_user(db)
    return current
