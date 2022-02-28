import hashlib
from common.MyGlobal import Global
from common.BaseApi import BaseApi

MyGlobal=Global()

class Request(BaseApi):
    def request_api(self,url,data):
        formdata=self.__get_formdata(data)
        return self.request(url, formdata)

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
