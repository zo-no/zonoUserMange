// 注册函数
function register() {
    // const serverURL = 'http://localhost:5000'; // 提取服务器地址,因为是挂载到后端所以不需要
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;

    // 发送注册请求到后端
    fetch('http://localhost:5000/api/v1/reg/', {
        method: "POST",
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
        .then(response => response.json())
        .then(data => alert(data.detail));
}

// 登录函数
function login() {
    //获取账号密码
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    //创建表单数据
    const data = new URLSearchParams();
    data.append('grant_type', '');
    data.append('username', username);
    data.append('password', password);
    data.append('scope', '');
    data.append('client_id', '');
    data.append('client_secret', '');

    // 发送登录请求到后端
    fetch("http://localhost:5000/api/v1/token", {
        method: "POST",
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: data
    })
        .then(response => response.json())
        .then(data => {
            const token = data.access_token;
            if (token) {
                localStorage.setItem("token", token);//储存token到本地
                alert("登录成功！");
            } else {
                alert("登录失败：" + data.detail);
            }
        });
}

// 获取用户信息函数
function getUserInfo() {
    const token = localStorage.getItem("token");

    if (token) {
        // 发送令牌以获取用户信息
        fetch("http://localhost:5000/api/v1/users/me", {
            method: 'GET',
            headers: {
                'accept': 'application/json',
                'Authorization': "Bearer " + token
            }
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data[0].username) {
                    document.getElementById("user-info").innerHTML = "用户名: " + data[0].username;
                } else {
                    document.getElementById("user-info").innerHTML = "无法获取用户信息。";
                }
            });
    } else {
        document.getElementById("user-info").innerHTML = "用户未登录。";
    }
}

