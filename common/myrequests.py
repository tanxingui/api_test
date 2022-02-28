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











