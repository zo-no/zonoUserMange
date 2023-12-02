/*
@Date		:2023/11/25 10:58:21
@Author		:zono
@Description:用户初始化调用接口（与后端对于）
*/

// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取当前的用户 GET /api/currentUser */
export async function currentUser(options?: { [key: string]: any }) {
  let token = localStorage.getItem('token');
  return request<{
    data: API.CurrentUser;
  }>('/api/v1/currentUser', {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      Authorization: 'Bearer ' + token,
    },
    ...(options || {}),
  });
}

/** 退出登录接口 POST /api/login/outLogin */
export async function outLogin(options?: { [key: string]: any }) {
  //删除token
  localStorage.removeItem('token');
  return request<Record<string, any>>('/api/v1/logout', {
    method: 'POST',
    ...(options || {}),
  });
}

/** 登录接口 POST /api/login/account */
/**
 * 获取令牌
 * @param body 请求体参数
 * @param options 请求配置选项
 * @returns 令牌响应数据
 */
export async function login(
  body: API.GetToken,
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

  return request<API.putToken>('/api/v1/login/account', {
    method: 'POST',
    data: formData,
    ...(options || {}),
  });
}

/** 注册接口 @description  :
@param  :
username:学号
password:密码
@Returns  :
------- POST /api/v1/reg/ */
export async function register(
  body: API.UserInDB,
  options?: { [key: string]: any },
) {
  return request<API.Response>('/api/v1/reg/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}
