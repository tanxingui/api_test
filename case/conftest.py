import pymysql
import pytest
from data.login_data import LoginData
from common.BaseApi import BaseApi

from common.MyGlobal import Global

MyGlobal=Global()
MyRequest=BaseApi()
login_data=LoginData
send_success_data=login_data.login_success_data
@pytest.fixture(scope="class")
def getloginsign():
    username,password=send_success_data[0]
    data = {
        "data": '{'
                '"username":"' + username + '",'
                '"password":"' + password + '",'
                '"captcha_text":"123456",'
                '"captcha_key":"5a3c82b303c5446a9295eddb134851db"'
                '}'
    }
    url = 'http://api.s.youcheyihou.com/testapi/iyourcar_autobuy/backend/login'
    result=MyRequest.request(url=url,data=data)
    # 获取token值
    token = result.json()["result"]["token"]
    sid = result.json()["result"]["sid"]
    MyGlobal.setLoginSid(sid)
    MyGlobal.setToken(token)
    return token, sid



