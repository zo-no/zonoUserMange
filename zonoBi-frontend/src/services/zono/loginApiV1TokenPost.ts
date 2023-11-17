// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取Token @description  :
登录接口,并返回Token
@param  :
-------
@Returns  :
access_token POST /api/v1/token */
export async function loginApiV1TokenPost(
  body: API.BodyLoginApiV1TokenPost,
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

  return request<API.Token>('/api/v1/token', {
    method: 'POST',
    data: formData,
    ...(options || {}),
  });
}
