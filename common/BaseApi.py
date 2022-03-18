
import requests
import json
from common.BaseRemind  import Remind
MyRemind=Remind()
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
                print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            else:
                print("只能支持post请求与get请求~")
        except AttributeError as e:
            print(e)
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

    def format_cases(self, cases):
        """{"id":0,"url":"","case_name":"","header":"","method":"","body":"",
        "expect":"","actual":"","valiadate":"","is_replace":"","is_perform":""},"""
        """抛出异常"""
        key_list = ["id", "url", "case_name", "header","method","body","expect","actual","valiadate"]
        for index, tuple_data in enumerate(cases):
            MyRemind.Exception_class(key_list, tuple_data)
            cases[index] = self.format_list(tuple_data)
        return cases

    def format_list(self,tuple_data):
        str_list = list(tuple_data)
        for index, data in enumerate(str_list):
            if type(data) == str:
                mm = data.replace("\n", "")
                str_list[index] = mm
        return tuple(str_list)
    def merge_list_dict(self,list_dict1,list_dict2):
        new_list_dict=[]
        for i in range(len(list_dict1)):
            list_dict1[i] |= list_dict2[i]
            new_list_dict.append(list_dict1[i])
        return new_list_dict




