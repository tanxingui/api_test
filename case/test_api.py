import json
import pytest
import jsonpath
from common.MyGlobal import Global
from common.BaseFormdata import Request
from case.conftest import getloginsign
MyRequest=Request()
MyGlobal=Global()
class Test_api:
    def __init__(self):
        token, sid = getloginsign()
        MyGlobal.setLoginSid(sid)
        MyGlobal.setToken(token)
    def test_api_01(self):
        data='{"page_id":1,"page_size":10,"querys":[{"col":"name","cond":"like","val":"深圳市科治好连锁有限公司"}]}'
        url="http://api.s.youcheyihou.com/testapi/iyourcar_autobuy/backend/chain_corp/list"
        MyRequest.request_api(url,data)
        # print(json.dumps(result.json(), indent=2, ensure_ascii=False))
        # json3 = jsonpath.jsonpath(result.json(), "$..name")

if __name__ == '__main__':
    t1=Test_api()
    t1.test_api_01()










