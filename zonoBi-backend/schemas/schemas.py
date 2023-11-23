# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/04 22:24:17
@Author		:zono
@Description:规范输入和输出，用户请求时要遵守对应的规范，方便进入数据库，当api响应时，也得依循该模型，并返回对应格式
'''
from typing import Union, Optional, List
from datetime import datetime
from datetime import date as date_type
from pydantic import BaseModel, Field

# ---------------------------------------------------------------
# TODO pydantic校验用field，路径参数校验使用path，查询参数校验使用Query


class UserBase(BaseModel):
    """
    @description  :用户基础信息
    """
    username: str

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    password: str = Field(description='密码')  # 继承，响应中不包含该类


class UserRes(UserBase):
    """
    @description:
    请求用户后回复的响应体
    """
    id: int
    avatarUrl: str
    phone: str
    email: str
    userRole: bool
    userStatus: str
    update_time: datetime


class GetToken(BaseModel):
    """
    @description  :
    返回给用户的Token的模型
    """
    access_token: str
    token_type: str
    status: str


class articleBase(BaseModel):
    title: str
    channels_id: int
    content: str

    class Config:
        orm_mode = True


class articleCreate(articleBase):
    owner_id: int
    pass
