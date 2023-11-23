# -*- encoding: utf-8 -*-
'''
@Date		:2023/11/23 21:20:14
@Author		:zono
@Description:退出接口，存储数据，但目前没有
'''
from fastapi import APIRouter, Depends, HTTPException

logOUT = APIRouter(tags=["用户初始化"])


@logOUT.post("/logout")
async def logout():
    """
    @description  :
    退出登录
    """
    return {"message": "logout success"}
