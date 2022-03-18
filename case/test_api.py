import pytest
from common.BaseFormdata import Request
from common.MyExcel_ import ExcelUtil
from config.myconf import MyConf
import ast
MyRequest=Request()
MyConf_order=MyConf()
path=MyConf_order.getConf()
#MyConf_order.getConf()
MyExcel=ExcelUtil("/Users/luzhihao/api_test/data/单个订单待付款.xlsx")
# MyExcel=ExcelUtil("/root/api_test/data"+MyConf_order.getConf())
print(f"pytest的conf为{MyConf_order.getConf()}")
# MyExcel=ExcelUtil("/Users/luzhihao/api_test/data"+MyConf_order.getConf())
#/订单模块/单个车型订单.xlsx
class Test_api:
    """志豪调用后返回的是一个[{"cases":[{dict}]}]"""
    @pytest.mark.parametrize("excel",MyExcel.read_excel()[0]["cases"])
    def test_api_01(self,getloginsign,excel):
        """1是执行，0是跳过"""
        print(f"pytest的conf为{MyConf_order.getConf()}")
        if excel["is_perform"]== 1:
            MyRequest.request_api(url=excel["url"],
                                  data=excel["body"],
                                  expect=excel["expect"],
                                  actual=excel["actual"],
                                  run_result_txt=excel["valiadate"],
                                  is_replace=excel["is_replace"],
                                  id=excel["id"])












