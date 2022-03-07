import hashlib
import json

import jsonpath

from common.MyGlobal import Global
from common.BaseApi import BaseApi
from common.MyAssert import MyAssert
from common.text_util import write_txt,truncate_txt,read_txt
from common.BaseReplace import Replace_data
from common.BaseRemind import Remind
MyRemind=Remind()
MyReplace=Replace_data()
MyGlobal=Global()
MyAssert=MyAssert()

class Request(BaseApi):
    """请求、断言、写入结果"""
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

        formdata=self.__get_formdata(id,data)
        result=self.request(url, formdata,method=method,verify=verify,timeout=timeout)
        result_dict = eval(result.text)
        MyReplace.extract_data(id, is_replace, result_dict)
        MyRemind.response_info(id, result_dict)
        assertion=MyAssert.assert_expect(id,expect,actual,result.json())
        if assertion:
            # 将运行结果写入txt文件保存
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__pass|"))  # 用"__"符号间隔
        else:
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__fail|"))

    def __get_formdata(self, id,data):
        data=MyReplace.replace_case_with_re(id,data)
        sign = hashlib.md5((MyGlobal.getToken() + data).encode("utf-8")).hexdigest()
        MyGlobal.setSign(sign)
        formdata = {
            "sid": MyGlobal.getLoginSid(),
            "sign": MyGlobal.getSign(),
            "data": data
        }
        return formdata


    def eq(self):
        """"""
