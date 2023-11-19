// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取当前的用户 GET /api/currentUser */
export async function currentUser(options?: { [key: string]: any }) {
  return request<{
    data: API.CurrentUser;
  }>('/api/currentUser', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 退出登录接口 POST /api/login/outLogin */
export async function outLogin(options?: { [key: string]: any }) {
  return request<Record<string, any>>('/api/login/outLogin', {
    method: 'POST',
    ...(options || {}),
  });
};




// function loginAPI(formData: any) {
//   return 
// };

// async function getToken(body: API.LoginParams, options?: { [key: string]: any }) { 
  /*
  @Description: 获取token,并存入localStorage
  */
//   // console.log(body);
//   const { username, password } = body;
//   // console.log(username, password);
//   const requestData = {
//     grant_type: "",
//     username,
//     password,
//     scope: "",
//     client_id: "",
//     client_secret: "",
//   };
//   console.log(requestData);
//   //分布异步请求，并存入
//   const res = await request('/token',{
//         method: 'POST',
//         data: requestData,
//         headers: {
//           'accept': "application/json",
//           "Content-Type": "application/x-www-form-urlencoded",
//         },
//       });
//   // console.log(res);
//   return res.data.access_token;
// }

/** 登录接口 POST /api/login/account */
export async function login(body: API.LoginParams, options?: { [key: string]: any }) {
  // let tokenMsg = getToken(body, options); //获取token
  let tokenMsg = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJleHAiOjE3MDA0MDg4NTl9.kIu0NrteMDEXUkNuVRzQygIy8wHp9kkntiwkyQ9HIy0";
  console.log(tokenMsg);
  // if (token) {
  //   localStorage.setItem("token", token.data)
  // }
  return request('/users/me', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + tokenMsg,
    },
    // data: body,
    ...(options || {}),
  });
}

/** 此处后端没有提供注释 GET /api/notices */
export async function getNotices(options?: { [key: string]: any }) {
  return request<API.NoticeIconList>('/api/notices', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 获取规则列表 GET /api/rule */
export async function rule(
  params: {
    // query
    /** 当前的页码 */
    current?: number;
    /** 页面的容量 */
    pageSize?: number;
  },
  options?: { [key: string]: any },
) {
  return request<API.RuleList>('/api/rule', {
    method: 'GET',
    params: {
      ...params,
    },
    ...(options || {}),
  });
}

/** 新建规则 PUT /api/rule */
export async function updateRule(options?: { [key: string]: any }) {
  return request<API.RuleListItem>('/api/rule', {
    method: 'PUT',
    ...(options || {}),
  });
}

/** 新建规则 POST /api/rule */
export async function addRule(options?: { [key: string]: any }) {
  return request<API.RuleListItem>('/api/rule', {
    method: 'POST',
    ...(options || {}),
  });
}

/** 删除规则 DELETE /api/rule */
export async function removeRule(options?: { [key: string]: any }) {
  return request<Record<string, any>>('/api/rule', {
    method: 'DELETE',
    ...(options || {}),
  });
}
