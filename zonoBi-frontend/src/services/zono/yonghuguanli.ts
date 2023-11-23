// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Read Users Me @description  :
获取多名用户信息
@param  :
-------
@Returns  :
------- GET /api/v1/currentUsers */
export async function readUsersMeApiV1CurrentUsersGet(options?: { [key: string]: any }) {
  return request<any>('/api/v1/currentUsers', {
    method: 'GET',
    ...(options || {}),
  });
}
