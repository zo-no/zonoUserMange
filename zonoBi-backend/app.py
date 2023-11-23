# -*- encoding: utf-8 -*-
'''
@Date		:2023/09/26 19:15:11
@Author		:zono
@Description:主文件，程序于这里运行
'''
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import settings
from core import events, Router

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from fastapi import Request

import time
# TODO 解决问题待学习,这是为了跨域，但有问题
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],#想加哪个加哪个
#     allow_credentials=True,#允许使用证书
#     allow_method=["*"],#允许跨域方法
#     allow_headers=["*"]#允许的请求头
# )
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]  # 跨域的第二种办法

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    authorization=settings.PROJECT_AUTHOR,
    email=settings.PROJECT_EMAIL,
    swagger_ui_oauth2_redirect_url=settings.SWAGGER_UI_OAUTH2_REDIRECT_URL,
    middleware=middleware
)


# ----------------------------事件监听-----------------------------------
app.add_event_handler("startup", events.startup(app))
app.add_event_handler("shutdown", events.stopping(app))


# --------------------------静态文件-------------------------------------

# QUER 这个路径配置很奇怪，好像python文件的配置路径是以app为主，一切都是以app为基准
templates = Jinja2Templates(directory="static")


@app.get("/", tags=['模板引擎'])
def index(request: Request):
    """
    @description  :
    前后端不分离的模板引擎
    @param  :
    -------
    @Returns  :
    -------
    """
    return templates.TemplateResponse("index.html", {"request": request})


# --------------------------中间件-------------------------------------


# TODO待移入中间件文件中
@app.middleware("http")  # QUER这样写的话中间件会作用到该app的所有接口中
async def add_process_time_header(request: Request, call_next):
    """
    @description  :
    计算响应时间
    @param  :
    -------
    @Returns  :
    -------
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response  # 中间件记录响应时间


@app.get("/123", tags=['用于测试前端'])
def index(request: Request):
    """
    @description  :
    前后端不分离的模板引擎
    @param  :
    -------
    @Returns  :
    -------
    """
    return {
        "date": [
            {
                "id": 1,
                "name": "张三"
            },
            {
                "id": 2,
                "name": "李四"
            }
        ]
    }


# 挂了一个照片用于测试 http://localhost:5000/img/zono.jpg
app.mount("/img", StaticFiles(directory="img"),
          name="img")  # 静态文件的挂载，这样就可以访问静态文件了

app.include_router(Router.router)  # 导入路由

if __name__ == '__main__':
    uvicorn.run('app:app', host="0.0.0.0", port=5000, reload=True)
