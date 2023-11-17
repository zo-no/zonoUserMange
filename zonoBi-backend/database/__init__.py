# -*- encoding: utf-8 -*-
'''
@Date		:2023/09/22 16:57:56
@Author		:zono
@Description:数据库配置，目前用的sqlist
'''
# from fastapi import APIRouter,Depends,HTTPException,status

# from sqlalchemy.orm import Session
# from schemas import schemas

# #TODO  SQLAlchemy 不具有await直接使用的兼容性,想办法解决

# from crud import crud
# from database.sqlite import engine,Base,SessionLocal

# sql_app = APIRouter(tags=['数据库调用'])

# Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     """
#     @description  :
#     底层依赖，每个接口都会调用该函数，打开会话，然后关闭会话，由depends导入
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @sql_app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     """
#     @description  :
#     读取全部用户列表
#     @param  :
#     -------
#     @Returns  :
#     -------
#     """
#     users = crud.get_users(db, skip=skip, limit=limit)
#     #QUER 无法直接按数组的方式返回return users[0].id
#     return users

# @sql_app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     """
#     @description  :
#     读取单个用户
#     @param  :
#     -------
#     @Returns  :
#     -------
#     """
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="未找到该用户")
#     return db_user


# @sql_app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     """
#     @description  :
#     读取单个用户信息
#     @param  :
#     -------
#     @Returns  :
#     -------
#     """
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @sql_app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

