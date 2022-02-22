

class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "luzhihao",
            "123456"
        )
    ]

    login_fail_data = [
        (
            "yangmingsong",
            "",
            "请输入密码"
        ),
        (
            "",
            "yangmingsong",
            "请输入帐号"
        ),
        (
            "linux",
            "yangmingsong",
            "帐号或密码错误"
        )
    ]


if __name__ == '__main__':
    pass
