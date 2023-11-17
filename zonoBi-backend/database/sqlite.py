# -*- encoding: utf-8 -*-
'''
@Date		:2023/10/04 22:22:18
@Author		:zono
@Description:连接sqlite数据库
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"#数据库url
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf-8',echo=True,connect_args={"check_same_thread": False}#"check_same_thread": False只对sqlite使用，访问多线程
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,expire_on_commit=True)#数据库会话

# QUER 和主函数的区别Base = declarative_base(bind=engine,name="Base")
Base = declarative_base()#元类