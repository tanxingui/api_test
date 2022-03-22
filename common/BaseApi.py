
import requests
import json
import hashlib
from common.MyGlobal import Global
from common.BaseReplace import Replace_data
from common.BaseRemind  import Remind
from common.MyException import exception_utils
MyRemind=Remind()
MyReplace=Replace_data()
MyGlobal=Global()
class BaseApi(object):
    """封装一些内置方法"""
    def request(self, url, data,method='post',verify=False,timeout=10):
        """request 请求api"""
        # print("\n")
        print('\ninfo:request api "{}"'.format(url))
        try:
            if method.upper() == "GET":
                result=requests.request(method=method,url=url,params=data,verify=verify,timeout=timeout)
                if "请重新登录" in str(result.json()):
                    MyRemind.request_error(data)

                else:
                    pass
                # print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            elif method.upper() == "POST":
                result = requests.request(method=method, url=url, data=data, verify=verify, timeout=timeout)
                if "请重新登录" in str(result.json()):
                    MyRemind.request_error(data)
                    print(data)
                else:
                    pass
                # print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            else:
                print("只能支持post请求与get请求~")
        except AttributeError as e:
            print(e)

    @exception_utils
    def get_formdata(self, data, is_replace):
        data = MyReplace.replace_case_with_re(data, is_replace)
        sign = hashlib.md5((MyGlobal.getToken() + data).encode("utf-8")).hexdigest()
        MyGlobal.setSign(sign)
        formdata = {
            "sid": MyGlobal.getLoginSid(),
            "sign": MyGlobal.getSign(),
            "data": data
        }
        return formdata

    def assert_all(self,actual,check):
        """alone assert"""
        "元素在元素中 返回True与False"
        if check["type"] == "eq":
            return actual == check["expected"]
        elif check["type"] == "in":
            return check["expected"] in actual

        else:
            print("type类型错误~")
            return False

    def merge_list_dict(self,list_dict1,list_dict2):
        new_list_dict=[]
        for i in range(len(list_dict1)):
            list_dict1[i] |= list_dict2[i]
            new_list_dict.append(list_dict1[i])
        return new_list_dict






