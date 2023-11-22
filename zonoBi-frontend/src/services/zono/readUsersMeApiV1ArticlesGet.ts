// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 文章获取 @description  :
一般用户
@param  :
-------
@Returns  :
------- GET /api/v1/articles */
export async function readUsersMeApiV1ArticlesGet(options?: { [key: string]: any }) {
  return request<any>('/api/v1/articles', {
    method: 'GET',
    ...(options || {}),
  });
}
