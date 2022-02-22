
import pytest
from common.BaseFormdata import Request
from case.conftest import getloginsign
MyRequest=Request()
class Test_api:
    def test_api_01(self):
        token,sid=getloginsign()
        data='{"page_id":1,"page_size":10,"querys":[{"col":"name","cond":"like","val":"深圳市科治好连锁有限公司"}]}'
        url="http://api.s.youcheyihou.com/testapi/iyourcar_autobuy/backend/chain_corp/list"
        MyRequest.request_api(url,data,token,sid)

if __name__ == '__main__':
    t1=Test_api()
    t1.test_api_01()










