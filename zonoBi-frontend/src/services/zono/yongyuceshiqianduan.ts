// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Index @description  :
前后端不分离的模板引擎
@param  :
-------
@Returns  :
------- GET /123 */
export async function index123Get(options?: { [key: string]: any }) {
  return request<any>('/123', {
    method: 'GET',
    ...(options || {}),
  });
}
