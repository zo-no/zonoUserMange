# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/04 22:26:59
@Author		:zono
@Description:对数据库的操作，#TODO接口对应操作
'''

from sqlalchemy.orm import Session

from models import base
from schemas import schemas


def get_user(db: Session, user_id: int):
    """
    @description  :
    通过id查找用户
    @param  :
    -------
    @Returns  :
    -------
    """
    return db.query(base.User).filter(base.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """
    @description  :
    通过用户名查找用户，有则返回true
    """
    return db.query(base.User).filter(base.User.username == username).first()  # 查询父表时要用到has()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    @description  :
    获取全部用户
    @param  :
    -------
    @Returns  :
    -------
    """
    return db.query(base.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInDB):
    """
    @description  :
    创建用户,只创建用户,不设置基础信息
    @param  :
    -------
    @Returns  :
    -------
    """
    db_user = base.User(username=user.username,
                        userPassword=user.password)  # TODO后面用解包的方式导入数据
    db.add(db_user)  # 见过实例添加到数据库，和上传github很像
    db.commit()  # 对数据库提交
    db.refresh(db_user)  # 刷新实例，例如会生成ID
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    @description  :
    获取全部表
    @param  :
    -------
    @Returns  :
    -------
    """
    return db.query(base.Item).offset(skip).limit(limit).all()


def create_article(db: Session, article_data: schemas.articleCreate):
    db_article = base.Article(**article_data.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_article(db: Session):
    """
    @description  :
    获取对应用户所有表
    @param  :
    -------
    @Returns  :
    -------
    """
    dbu = db.query(base.User).get(1)
    return dbu.articles[2]


if __name__ == "__main__":
    # 增
    s = base.User({
        "username": "string",
        "password": "string"
    })  # 创建对象
    db.Session.add(s)  # 添加
    db.Session.commit()  # 提交
# ---------------------------------------------------------------
