# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/07 16:26:03
@Author		:zono
@Description:输出文章列表、输出文章内容
'''
from fastapi import APIRouter, Depends, HTTPException, status


articleOutput = APIRouter()


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

#TODO artcleOutput