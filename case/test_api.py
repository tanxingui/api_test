import pytest
from Controller.ControllerRequest import Request
from common.MyExcel_ import ExcelUtil
from config.myconf import MyConf
from config.mypath import *
from common.yaml_util import *
MyRequest=Request()
excel=merge_yaml()
#yaml_file=os.path.join(yaml_dir,'单个订单待付款.yaml')
#excel=read_yaml(yaml_file)["cases"]
"""志豪调用后返回的是一个[{"cases":[{dict}]}]"""
@pytest.mark.parametrize("excel",excel)
def test_api_01(getloginsign,excel):
    """1是执行，0是跳过"""
    if excel["is_perform"]== 1:
        MyRequest.request_api(url=base_url+excel["url"],
                              data=excel["body"],
                              expect=excel["expect"],
                              actual=excel["actual"],
                              run_result_txt=excel["valiadate"],
                              is_replace=excel["is_replace"],
                              id=excel["id"])












