// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Read Users Me @description  :
一般用户
@param  :
-------
@Returns  :
------- GET /api/v1/users/me */
export async function readUsersMeApiV1UsersMeGet(options?: { [key: string]: any }) {
  return request<any>('/api/v1/users/me', {
    method: 'GET',
    ...(options || {}),
  });
}
