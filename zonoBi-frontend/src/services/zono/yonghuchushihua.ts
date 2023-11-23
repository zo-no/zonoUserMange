// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取当前用户 @description  :
一般用户
@param  :
-------
@Returns  :
------- GET /api/v1/currentUser */
export async function readUsersMeApiV1CurrentUserGet(options?: { [key: string]: any }) {
  return request<any>('/api/v1/currentUser', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 获取Token @description  :
登录接口,设置过期时间,并返回Token和登录状态
@param  :
-------
@Returns  :
access_token POST /api/v1/login/account */
export async function loginApiV1LoginAccountPost(
  body: API.BodyLoginApiV1LoginAccountPost,
  options?: { [key: string]: any },
) {
  const formData = new FormData();

  Object.keys(body).forEach((ele) => {
    const item = (body as any)[ele];

    if (item !== undefined && item !== null) {
      if (typeof item === 'object' && !(item instanceof File)) {
        if (item instanceof Array) {
          item.forEach((f) => formData.append(ele, f || ''));
        } else {
          formData.append(ele, JSON.stringify(item));
        }
      } else {
        formData.append(ele, item);
      }
    }
  });

  return request<API.GetToken>('/api/v1/login/account', {
    method: 'POST',
    data: formData,
    ...(options || {}),
  });
}

/** 注册接口 @description  :
注册接口，对传入的账号密码进行审核后注册，如果数据库无该用户就允许注册
并把数据加入数据库，密码哈希一次，
校验交给前端吧。
也可以https://blog.csdn.net/qq_39147299/article/details/117438065
@param  :
username:学号
password:密码
@Returns  :
------- POST /api/v1/reg/ */
export async function registrationApiV1Reg_post(
  body: API.UserInDB,
  options?: { [key: string]: any },
) {
  return request<API.UserInDB>('/api/v1/reg/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}
