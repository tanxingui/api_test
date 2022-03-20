import pytest
from Controller.ControllerRequest import Request
from common.MyExcel_ import ExcelUtil
from config.myconf import MyConf
from config.mypath import *

MyRequest=Request()
MyConf_order=MyConf()
#MyConf_order.getConf()
# MyExcel=ExcelUtil(testdata_dir+MyConf_order.getConf())

MyExcel=ExcelUtil(os.path.join(testdata_dir,"单个订单待付款.xlsx"))
class Test_api:
    """志豪调用后返回的是一个[{"cases":[{dict}]}]"""
    @pytest.mark.parametrize("excel",MyExcel.read_excel()[0]["cases"])
    def test_api_01(self,getloginsign,excel):
        """1是执行，0是跳过"""
        if excel["is_perform"]== 1:
            MyRequest.request_api(url=excel["url"],
                                  data=excel["body"],
                                  expect=excel["expect"],
                                  actual=excel["actual"],
                                  run_result_txt=excel["valiadate"],
                                  is_replace=excel["is_replace"],
                                  id=excel["id"])












