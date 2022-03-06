import json
import pytest
from common.MyGlobal import Global
from common.BaseFormdata import Request
from common.MyExcel_ import ExcelUtil
MyRequest=Request()
MyGlobal=Global()
MyExcel=ExcelUtil("/Users/luzhihao/api_test/data/api_demo.xlsx")

class Test_api:
    """志豪调用后返回的是一个[{"cases":[{dict}]}]"""
    @pytest.mark.parametrize("excel",MyExcel.read_excel()[0]["cases"])
    def test_api_01(self,getloginsign,excel):
        data=excel["body"]
        url=excel["url"]
        MyRequest.request_api(url,data,expect=excel["expect"],run_result_txt=excel["valiadate"],id=excel["id"])











