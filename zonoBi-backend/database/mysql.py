# -*- encoding: utf-8 -*-
'''
@Date			:2023/09/22 16:56:21
@Author		    :zono
@Description	:连接mysql数据库
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -----------------------数据库配置-----------------------------------
USER='debian-sys-maint'
PWD='Mjul3R5SIVmqFAXu'
DB_NAME='login_app'

SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{USER}:{PWD}@localhost:3306/{DB_NAME}?charset=utf8&auth_plugin=mysql_native_password'#mysql
# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


