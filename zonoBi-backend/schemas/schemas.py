# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/04 22:24:17
@Author		:zono
@Description:规范输入和输出，用户请求时要遵守对应的规范，方便进入数据库，当api响应时，也得依循该模型，并返回对应格式
'''
from typing import Union
from datetime import datetime
from datetime import date as date_type
from pydantic import BaseModel, Field

# ---------------------------------------------------------------
# TODO pydantic校验用field，路径参数校验使用path，查询参数校验使用Query


class Token(BaseModel):
    """
    @description  :
    返回给用户的Token
    """
    access_token: str
    token_type: str


class UserBase(BaseModel):
    """
    @description  :用户类
    """
    username: str


class UserInDB(UserBase):
    password: str = Field(description='密码')  # 继承，响应中不包含该类


class User(UserBase):
    """
    @description:
    回复的响应体
    """
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# class Item(ItemBase):
#     """
#     @description  :
#     表读取
#     """
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True#配置，告诉Pydantic，该类不是dict，而是ORM模型，读取数据不是data[id]，而是data.id


class articleBase(BaseModel):
    title: str
    channels_id: int
    content: str

    class Config:
        orm_mode = True


class articleCreate(articleBase):
    owner_id: int
    pass
