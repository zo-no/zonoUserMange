# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-
'''
@Date		:2023/11/16 16:57:17
@Author		:zono
@Description:数据库配置
'''

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, func
from sqlalchemy.orm import relationship

from database.sqlite import Base


class User(Base):  # 元类
    """
    @description  :
    用户表：
    id:用户id,自增长
    username:用户名不可空、注解
    hashed_password:密码
    is_active:权限
    """
    # 表名
    __tablename__ = "users"
    # 字段
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")#关联表Item
    # # 创建时间
    # create_at = Column(DateTime, default=datetime.datetime.now)
    # # 更新时间
    # update_at = Column(DateTime, default=datetime.datetime.now,
    #                    onupdate=datetime.datetime.now)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())  # 只在更新时调用

    # __mapper_args__ = {
    #     'order_by': id.desc()# 按id倒序排列
    # }

    # def __repr__(self):
    #     return f"<User {self.id}>"


class Article(Base):
    """
    @description  :
    文章表：
    id:文章id,自增长
    table:用户名不可空、注解
    hashed_password:密码
    is_active:权限
    """
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    channels_id = Column(Integer)  # ForeignKey("channels.id"),
    content = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # TODO研究下relationship使用
    # owner = relationship("User", back_populates="Article")


# TODO 将想好的表创建

# # TODO 解决表的实时变动
# class User2(Base):  # 元类
#     """
#     @description  :
#     用户表：
#     id:用户id,自增长
#     username:用户名不可空、注解
#     userAccount:登录账号
#     avatarUrl:头像
#     gender 性别 tinyint
#     userPassword 密码 varchar
#     phone 电话 varchar
#     email 箱 varchar
#     userStatus 用户状态 int 0-正常
#     createTime 创建时间 (数据插入时间) datetime
#     updateTime 更新时间 (数据更新时间) datetime
#     isDelete 是否删除 0 1 (逻辑删除) tinyint
#     userRole 用户角色 0- 普通用户 1- 管理员
#     """
#     # 表名
#     __tablename__ = "users"
#     # 字段
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     username = Column(String, unique=True, index=True, nullable=False)
#     userPassword = Column(String)
#     phone = Column(Integer)
#     email = Column(String)
#     userStatus = Column(Integer)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now(),
#                         onupdate=func.now())  # 只在更新时调用
#     isDelete = Column(Boolean, default=True)
#     userRole = Column(Boolean, default=True)
