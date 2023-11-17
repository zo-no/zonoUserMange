# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-
'''
@Date		:2023/11/06 13:56:18
@Author		:zono
@Description:接收文章并存储到服务器数据库
'''
from fastapi import APIRouter, Depends, HTTPException, status

# ---------------------------------------------------------------
from sqlalchemy.orm import Session
from database.sqlite import engine, Base, SessionLocal

from crud import crud
from models import base
from schemas import schemas


articleInput = APIRouter()

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



@articleInput.post("/artcleInput",status_code=200, summary="文章传入")
async def articlInput(article_data: schemas.articleCreate,db: Session = Depends(get_db)):
    """
    @description  :
    接收文章并存储
    @param  :
    -------
    @Returns  :
    -------
    """
    crud.create_article(db=db, article_data=article_data)
    # TODO article_data不能改为article，为什么，就算我是把crud中对应的位置改了也是
    return "Ok"
