// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

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
  return request<API.User>('/api/v1/reg/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}
