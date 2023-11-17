# -*- encoding: utf-8 -*-
'''
@Date		:2023/09/26 18:28:37
@Author		:zono
@Description:基本配置文件
'''
import os
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings
from typing import List

class Config(BaseSettings):
  
  load_dotenv(find_dotenv(), override=True)# 加载环境变量
  
  APP_DEBUG: bool = True# 调试模式

  # 项目信息
  PROJECT_NAME: str = "Zono的用户管理后台"
  PROJECT_VERSION: str = "1.0.0"
  PROJECT_DESCRIPTION: str = "用户管理后台"
  PROJECT_AUTHOR: str = "zono"
  PROJECT_EMAIL: str = "2742160682@qq.com"

  # 静态资源目录
  STATIC_DIR: str =  "./static/templates"
  # TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")

  # TODO 还未联系
  SWAGGER_UI_OAUTH2_REDIRECT_URL = "/api/v1/token"
  # Session
  pass

  # Jwt
  SECRET_KEY="zono"#TODO
  ALGORITHM = "HS256"#算法变量
  ACCESS_TOKEN_EXPIRE_MINUTES = 30#过期时间


  pass

  # 跨域设置
  CORS_ORIGINS: List = [
        "http://localhost:3000"
        "http://127.0.0.1:3000"
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "*"
    ]#配置跨域要求
  # CORS_ALLOW_CREDENTIALS: bool = True
  # CORS_ALLOW_METHODS: List = ["*"]
  # CORS_ALLOW_HEADERS: List = ["*"]
  pass

  # 二维码 
  pass


settings = Config()