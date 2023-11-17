# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: api路由导出区
"""
from fastapi import APIRouter

from .v1 import v1

api_router = APIRouter(
                    # dependencies=[Depends(***)]#该路由下所有接口的依赖
                    # response={200,{"msg":"good"}}#作用到所有接口的响应
                       )

api_router.include_router(v1,prefix="/api")

# from .backgroundTasks import Back_app#用于学习，日后迭代用
# api_router.include_router(Back_app,tags=["后台测试模块"])