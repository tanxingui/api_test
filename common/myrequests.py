import hashlib
import os.path
import requests
import logging
from common.myDATA import DATA
from common.myconf import MyConf
from common.mypath import conf_dir




class Myrequests:
    def __init__(self):
        self.url=MyConf(os.path.join(conf_dir, "conf.ini")).get("server", "host")

    def send_requests(self,Method,apiurl,data,token=None):

        url=self.url+apiurl
        logging.info("请求url: \n{}".format(url))
        logging.info("请求方法: \n{}".format(Method))

        if Method.upper() == "GET":
            resp = requests.request(Method, url, params=data)
        else:
            resp = requests.request(Method, url, data=data)
        return resp

    def getsigndata(self,sid,token,data):
        sign = hashlib.md5((token + data).encode("utf-8")).hexdigest()
        data=eval(data)
        data["sid"] = sid
        data["sign"] = sign
        return data
    def getsidtoken(self):
        sid=getattr(DATA,"sid")
        token=getattr(DATA,"token")

        return sid,token

    def getdata(self,sid,sign,data):
        data={'sid':sid,'sign':sign,'data':data}
        return data



# if __name__ == '__main__':
#     AA=Myrequests()
#     data = {
#         "data": '{'
#                 '"username":"yangmingsong",'
#                 '"password":"123456",'
#                 '"captcha_text":"123456",'
#                 '"captcha_key":"5a3c82b303c5446a9295eddb134851db"'
#                 '}'
#     }
#     print(type(data))
#
#     url="iyourcar_autobuy/backend/login"
#     p="post"
#     print( AA.send_requests(p,url,data).json())










