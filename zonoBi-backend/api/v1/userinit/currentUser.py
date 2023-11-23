# -*- encoding: utf-8 -*-
'''
@Date		:2023/11/23 17:27:41
@Author		:zono
@Description:当前用户接口
'''
from datetime import datetime, timedelta
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status


# ---------------------数据库有关的导入------------------------------------------
from sqlalchemy.orm import Session

from database.sqlite import engine, Base, SessionLocal

from crud import crud
from models import base
from schemas import schemas

# ----------------------------有关安全的导入-----------------------------------
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

currentUser = APIRouter()

Base.metadata.create_all(bind=engine)

# TODO 加入配置文件中------------------------初始化设置---------------------------------------
SECRET_KEY = "efb8d310a2e46e859a8e2f196ad25ff41916c90828999d64d50699f4f6cae93c"  # TODO 加入配置中
ALGORITHM = "HS256"  # 算法变量
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 过期时间


pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto")  # 使用bcrypt算法对密码加密
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login/account")  # 用户校验地址
# 数据库的打开和关闭


def get_db():
    """
    @description  :
    底层依赖，每个接口都会调用该函数，打开会话，然后关闭会话，由depends导入
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    @description  :
    校验Token，验证用户，并获取当前用户
    @param  :
    -------
    @Returns  :
    -------
    """
    # TODO 获取用户量可以设置,调整对应用户才能使用对应数据
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据，可能是登录过期,或者用户已注销",  # TODO 日后完善
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[
                             ALGORITHM])  # 与encode反过来
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        # XXX获取所有用户 token_data = crud.get_users(db, skip=0, limit=100)
        token_data = crud.get_user_by_username(db, username)
        # TODO修改为只取对应用户
    except JWTError:
        raise credentials_exception
    return token_data

# ---------------------------------------------------------------


async def get_current_active_user(current_user: schemas.UserRes = Depends(get_current_user)):
    """
    @description  :
    对获取的数据进行判断
    1.是否为活跃用户
    2.是否为管理员
    @param  :
    -------
    @Returns  :
    -------
    """
    current_user.userPassword = None  # 删除密码字段
    if current_user.isDelete != 0:
        raise HTTPException(status_code=400, detail="用户已注销")
    return current_user


@currentUser.get("/currentUser")
async def read_users_me(current_user: schemas.UserRes = Depends(get_current_active_user)):
    """
    @description  :
    一般用户
    @param  :
    -------
    @Returns  :
    -------
    """
    #     name: 'Serati Ma',
    #     avatar: 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
    #     userid: '00000001',
    #     email: 'antdesign@alipay.com',
    #     signature: '海纳百川，有容乃大',
    #     title: '交互专家',
    #     group: '蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED',
    #     tags: [
    #         {
    #           key: '0',
    #             label: '很有想法的',
    #         },
    #         {
    #             key: '1',
    #             label: '专注设计',
    #         },
    #         {
    #             key: '2',
    #             label: '辣~',
    #         },
    #         {
    #             key: '3',
    #             label: '大长腿',
    #         },
    #         {
    #             key: '4',
    #             label: '川妹子',
    #         },
    #         {
    #             key: '5',
    #             label: '海纳百川',
    #         },
    #     ],
    #     notifyCount: 12,
    #     unreadCount: 11,
    #     country: 'China',
    #     access: getAccess(),
    #     geographic: {
    #         province: {
    #             label: '浙江省',
    #             key: '330000',
    #         },
    #         city: {
    #             label: '杭州市',
    #             key: '330100',
    #         },
    #     },
    #     address: '西湖区工专路 77 号',
    #     phone: '0752-268888888',
    # }
    return current_user
