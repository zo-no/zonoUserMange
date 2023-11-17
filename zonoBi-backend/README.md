# fastapi用户管理

#### 介绍

用户管理后台

#### 软件架构

<!-- - api 
  - userManage
  - articleManage 
  - 其他的几个都是练手的库后面会改
- app.py -- 启动应用
- config.py
- db -- 数据库
- model -- 模型
- utils -- 工具 -->

```c
.
├── api -- 接口库
│   ├── api.py -- 练手的库后面会删
│   ├── articleManage -- 文章管理库
│   ├── backgroundTasks.py -- 练手的库后面会删
│   └── userManage -- 用户管理api库
├── core
│   ├── events.py -- 事件
│   ├── exception.py
│   ├── Middleware.py -- 中间件
│   └── Router.py -- 全局路由
├── crud -- 增删查改
├── database -- 数据库
├── models -- 与数据库交互类
├── schemas -- 响应类
├── static -- 静态文件库
├── config.py -- 配置
└── app.py -- 启动应用
```


#### 安装教程

配置基本python环境，3.10以上都成功运行，其他的没看
1. pip install -r requirements.txt
2. python app.py

#### 使用说明

1. 我自己使用的端口是5000，可以去app.py中修改
2. 访问xxx:5000,可以看见一个简单的前端注册登录界面
3. 还有很多基础设置未修改，敬请期待


#### Todo

- [x] 完成基础脚手架搭建
- [ ] 完成用户管理功能
  - [x] 基础注册功能
  - [ ] 登录功能

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

#### 提醒自己上传代码

1.分支操作

```cmd
git branch 'new branch'#新建分支
git branch #查看分支，名称前面加* 号的是当前的分支
git branch -a #查看所有分支
git checkout 'new branch'#切换分支
git checkout -b 'new branch'#新建并切换分支
git merge 'new branch'#合并分支
git branch -d 'new branch'#删除分支
```

2.上传代码并打个tag

```cmd
git add .
git commit -m "first commit"
git push origin <指定的分支名>
git push gitee master
git push github master
```

加-f：force强制推送

3.从远程指定分支上拉取代码

```cmd
git clone -b  <指定分支名>  <ssh或者http地址> 
```

git push gitee master
git push github master

<!-- #### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/) -->
