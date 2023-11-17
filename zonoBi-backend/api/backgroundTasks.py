# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/05 17:27:20
@Author		:zono
@Description:后台任务示例
'''
from typing import Annotated
from fastapi import BackgroundTasks, APIRouter,Depends

Back_app = APIRouter()

def write_log(message:str):
    """
    @description  :
    写入log,log日志
    @param  :
    -------
    @Returns  :
    -------
    """
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    """
    @description  :
    查找问题，并调用write_log写入log中
    @param  :
    -------
    @Returns  :
    -------
    """
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q

@Back_app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    """
    @description  :
    输入邮箱，和对应的内容，然后后台运行存入log中
    @param  :
    -------
    @Returns  :
    -------
    """
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}




# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)

# @Back_app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(# 将任务函数传到 后台任务 对象中
#         write_notification,# 后台运行的任务函数
#         email, # 按顺序传递给任务函数的任意参数序列
#         message="some notification") # 传递给任务函数的任意关键字参数
#     return {"message": "Notification sent in the background"}
