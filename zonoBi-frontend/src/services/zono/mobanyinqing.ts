// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Index @description  :
前后端不分离的模板引擎
@param  :
-------
@Returns  :
------- GET / */
export async function index_get(options?: { [key: string]: any }) {
  return request<any>('/', {
    method: 'GET',
    ...(options || {}),
  });
}
