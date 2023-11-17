// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 文章传入 @description  :
接收文章并存储
@param  :
-------
@Returns  :
------- POST /api/v1/artcleInput */
export async function articlInputApiV1ArtcleInputPost(
  body: API.articleCreate,
  options?: { [key: string]: any },
) {
  return request<any>('/api/v1/artcleInput', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}
