export default [
  {
    path: '/user',
    layout: false,
    routes: [
      { name: '登录', path: '/user/login', component: './User/Login' },
      { name: '注册', path: '/user/reg', component: './User/register' },
    ],
  },
  { name: '欢迎界面', path: '/welcome', icon: 'smile', component: './Welcome' },
  {
    path: '/admin',
    icon: 'crown',
    access: 'canAdmin',
    name: '管理员界面',
    routes: [
      { path: '/admin', redirect: '/admin/sub-page' },
      { path: '/admin/sub-page', component: './Admin' },
      { path: '/admin/user-manage', name: '用户管理', component: './Admin/Usermange' },
    ],
  },
  { icon: 'table', path: '/list', component: './TableList', name: '表格页' },
  { path: '/', redirect: '/welcome' },
  { path: '*', layout: false, component: './404' },
];
