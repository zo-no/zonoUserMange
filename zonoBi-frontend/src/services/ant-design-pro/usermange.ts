// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Read Users Me @description  :
获取多名用户信息
@param  :
-------
@Returns  :
------- GET /api/v1/currentUsers */
export async function CurrentUsersGet(options?: { [key: string]: any }) {
  let token = localStorage.getItem('token');
  return request<any>('/api/v1/currentUsers', {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      Authorization: 'Bearer ' + token,
    },
    ...(options || {}),
  });
}
