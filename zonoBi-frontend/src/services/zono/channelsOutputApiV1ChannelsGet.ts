// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 文章频道 @description  :
返回频道分类
@param  :
-------
@Returns  :
------- GET /api/v1/channels */
export async function channelsOutputApiV1ChannelsGet(options?: { [key: string]: any }) {
  return request<any>('/api/v1/channels', {
    method: 'GET',
    ...(options || {}),
  });
}
