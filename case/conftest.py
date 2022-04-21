import time

import pymysql
import pytest
from data.login_data import LoginData
from common.BaseApi import BaseApi
import os
from common.MyGlobal import Global

MyGlobal=Global()
MyRequest=BaseApi()
login_data=LoginData
send_success_data=login_data.login_success_data
@pytest.fixture(scope="function")
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
    yield

# @pytest.fixture(scope='session', autouse=True)
# def truncate():
#     """运行用例前清空data下的相关文件"""
#     print("\n用例运行前操作：")
#     print("1.清空run_result.txt文件")
#     truncate_txt("%s/data/run_result.txt" % base_dir)
#     print("2.清空extract_save.txt文件")
#     truncate_txt("%s/data/extract_save.txt" % base_dir)
#     print("3.清空extract_replace.txt文件")
#     truncate_txt("%s/data/extract_replace.txt" % base_dir)
#     print("4.清空extract.ymal文件")
#     truncate_txt("%s/data/data_driven_yaml/extract.yaml" % base_dir)
#     yield
#     print("用例运行完毕，这是后置")



