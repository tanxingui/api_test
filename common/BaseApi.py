
import requests
import json

class BaseApi(object):
    """结合显示等待封装一些内置方法"""
    def request(self, url, data,method='post',verify=False,timeout=10):
        """request 请求api"""
        print('info:request api "{}"'.format(url))
        try:
            if method.upper() == "GET":
                result=requests.request(method=method,url=url,params=data,verify=verify,timeout=timeout)
                if "请重新登录" in str(result.json()):
                    print("请检查url是否输入正确")
                else:
                    pass
                print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            elif method.upper() == "POST":
                result = requests.request(method=method, url=url, data=data, verify=verify, timeout=timeout)
                if "请重新登录" in str(result.json()):
                    print("请检查url是否输入正确")
                else:
                    pass
                print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            else:
                print("只能支持post请求与get请求~")
        except AttributeError as e:
            print(e)
    def assert_in(self):
        """alone assert"""
        "元素在元素中 返回True与False"
    def assert_eq(self):
        """alone assert"""
        "元素在元素中"
    def mysql_select(self):
        """获取sql，返回result"""



