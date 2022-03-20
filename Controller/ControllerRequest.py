
import json
import jsonpath
from common.BaseApi import BaseApi
from common.MyAssert import MyAssert
from common.text_util import write_txt,truncate_txt,read_txt
from common.BaseReplace import Replace_data
from common.BaseRemind import Remind
from common.MyException import exception_utils
MyRemind=Remind()
MyAssert=MyAssert()
MyReplace=Replace_data()
class Request(BaseApi):
    """请求、断言、写入结果"""
    """is_replace:[{"is_extract":1,"extract_expr":"$.result.list[0].order_no","rely":"10_parent_order_no"}]"""
    """is_replace:[{"is_extract":0,"rely_list":["10_parent_order_no"]}]"""

    @exception_utils
    def request_api(self,
                    url,
                    data,
                    id,
                    expect=None,
                    actual=None,
                    is_replace=None,
                    run_result_txt=None,
                    method='post',
                    verify=False,
                    timeout=10
                    ):

        formdata=self.get_formdata(data,is_replace)
        result=self.request(url, formdata,method=method,verify=verify,timeout=timeout)
        result_dict = eval(result.text)
        MyReplace.extract_data(result_dict,is_replace)
        MyRemind.response_info(id, result_dict)
        assertion=MyAssert.assert_expect(id,expect,actual,result.json())
        if assertion:
            # 将运行结果写入txt文件保存
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__pass|"))  # 用"__"符号间隔
        else:
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__fail|"))



    def eq(self):
        """"""