import pytest
from common.BaseFormdata import Request
from common.MyExcel_ import ExcelUtil
import ast
MyRequest=Request()
MyExcel=ExcelUtil("/Users/luzhihao/笔记本桌面文件夹/卢志豪-接口用例管理/B端订单模块/单个车型订单.xlsx")

class Test_api:
    """志豪调用后返回的是一个[{"cases":[{dict}]}]"""
    @pytest.mark.parametrize("excel",MyExcel.read_excel()[0]["cases"])
    def test_api_01(self,getloginsign,excel):
        """1是执行，0是跳过"""
        actual_list = ast.literal_eval(excel["is_perform"])
        if actual_list[0]["is_perform"] == 1:
            data = excel["body"]
            url = excel["url"]
            MyRequest.request_api(url,
                                  data,
                                  expect=excel["expect"],
                                  actual=excel["actual"],
                                  run_result_txt=excel["valiadate"],
                                  is_replace=excel["is_replace"],
                                  id=excel["id"])
        else:
            pass











