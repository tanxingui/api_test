import hashlib
from common.BaseApi import BaseApi



class Request(BaseApi):
    def request_api(self,url,data,token,sid):
        formdata=self.__get_formdata(data,token,sid)
        return self.request(url, formdata)

    def __get_formdata(self, data, token, sid):
        sign3 = hashlib.md5((token + str(data)).encode("utf-8")).hexdigest()
        formdata = {
            "sid": sid,
            "sign": sign3,
            "data": str(data)
        }
        return formdata

    # def getsidtoken(self):
    #     sid = getattr(DATA, "sid")
    #     token = getattr(DATA, "token")
    #
    #     return sid, token

    def eq(self):
        """"""