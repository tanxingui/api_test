import pytest
from Controller.ControllerRequest import Request
from common.yaml_util import *
from common.MyException import exception_utils
MyRequest=Request()
MyExcel=ExcelUtil(os.path.join(excel_dir,'自动化用例.xlsx'))
"""【单个订单待付款，单辆车采购完成，单辆车待提车，整版订单待付款，整版订单待提车，自动化用例】"""
value=MyExcel.read_excel()
excel=value[0]["cases"]
@exception_utils
@pytest.mark.parametrize("excel_case",excel)
def test_api_01(getloginsign,excel_case):
    """志豪调用后返回的是一个[{"cases":[{dict}]}]"""
    """接口测试用例"""
    assertion=MyRequest.case_manage(
        case_name=excel_case["case_name"],
        request_list=excel_case["request_list"],
        assert_list=excel_case["assert"]
    )
    assert assertion












