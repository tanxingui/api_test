import hashlib
from common.MyGlobal import Global
from common.BaseApi import BaseApi
from common.MyAssert import MyAssert
from common.text_util import write_txt,truncate_txt,read_txt
MyGlobal=Global()
MyAssert=MyAssert()

class Request(BaseApi):
    """请求、断言、写入结果"""
    def request_api(self,url,data,id,expect=None,run_result_txt=None,method='post',verify=False,timeout=10):
        formdata=self.__get_formdata(data)
        result=self.request(url, formdata,method=method,verify=verify,timeout=timeout)
        assertion=MyAssert.assert_expect(expect,result.json())
        if assertion:
            # 将运行结果写入txt文件保存
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__pass|"))  # 用"__"符号间隔
        else:
            write_txt(text_file=run_result_txt, data=str(f"用例id__{id}__fail|"))


    def __get_formdata(self, data):
        sign = hashlib.md5((MyGlobal.getToken() + str(data)).encode("utf-8")).hexdigest()
        MyGlobal.setSign(sign)
        formdata = {
            "sid": MyGlobal.getLoginSid(),
            "sign": MyGlobal.getSign(),
            "data": str(data)
        }
        return formdata


    def eq(self):
        """"""
