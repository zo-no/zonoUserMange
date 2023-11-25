# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/26 21:50:18
@Author		:zono
@Description:转出api
目前有文章管理（开发ing）
用户登录注册
'''
from fastapi import APIRouter
from .userinit import *
from .userManage import *
from .articleManage import *

v1 = APIRouter(prefix="/v1")

# 用户初始化接口
v1.include_router(loginUP)  # 登录相关
v1.include_router(logOUT)  # 退出登录
v1.include_router(reg)  # 注册相关
v1.include_router(currentUser)  # 获取当前用户信息


# 用户管理接口
v1.include_router(currentUsers)  # 获取多名用户信息


# 文章管理接口
v1.include_router(articleOutput)
v1.include_router(articleInput)
