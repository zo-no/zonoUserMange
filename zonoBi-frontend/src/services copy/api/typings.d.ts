declare namespace API {
  type CurrentUser = {
    //获取用户信息的返回值
    id?: number;
    username?: string;
    avatarUrl?: string;
    phone?: string;
    email?: string;
    signature?: string;
    group?: string;
    tags?: { key?: string; label?: string }[];
    notifyCount?: number;
    unreadCount?: number;
    country?: string;
    userRole?: boolean;
    geographic?: {
      province?: { label?: string; key?: string };
      city?: { label?: string; key?: string };
    };
    address?: string;
  };

  type UserInDB = {
    //注册的参数
    username: string;
    password: string;
  };

  interface GetToken {
    //请求token的参数
    grant_type?: string;
    username: string;
    password: string;
    scope?: string;
    client_id?: string;
    client_secret?: string;
  }

  type putToken = {
    //请求token的返回值
    access_token: string;
    token_type: string;
    status: string;
  };

  type Response = {
    //通用的返回值（待完善）
    detail?: string;
  };
}
