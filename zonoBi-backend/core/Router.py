# -*- encoding: utf-8 -*-
'''
@Date		:2023/09/27 15:13:41
@Author		:zono
@Description:路由整合文件
'''
from fastapi import APIRouter


from api import api_router

router = APIRouter()

# API路由
router.include_router(api_router)


