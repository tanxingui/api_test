import requests
import hashlib
from common.MyGlobal import Global
from common.BaseReplace import Replace_data
from checkout.BaseRemind import Remind
from common.MyException import exception_utils
from common.BaseLog import LogUtil
MyRemind=Remind()
MyReplace=Replace_data()
MyGlobal=Global()
MyLog=LogUtil()
class BaseApi(object):
    last_result_json = None
    """封装一些内置方法"""
    """is_replace:[{"is_extract":1,"extract_expr":"$.result.list[0].order_no","rely":"10_parent_order_no"}]"""
    """is_replace:[{"is_extract":0,"rely_list":["10_parent_order_no"]}]"""
    def get_last_result_json(self):
        return  BaseApi.last_result_json
    def set_last_result_json(self, last_result_json1):
        BaseApi.last_result_json=last_result_json1
    def request(self, url, data,method='post',verify=False,timeout=10):
        """request 请求api"""
        # print("\n")
        # print('\ninfo:request api "{}"'.format(url))
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
                    # print(data)
                else:
                    pass
                # print(json.dumps(result.json(), indent=2, ensure_ascii=False))
                return result
            else:
                print("只能支持post请求与get请求~")
        except AttributeError as e:
            print(e)

    @exception_utils
    def request_api(self,
                    name,
                    url,
                    data,
                    is_replace=None,
                    method='post',
                    verify=False,
                    timeout=10
                    ):

        formdata = self.get_formdata(data)
        result = self.request(url, formdata, method=method, verify=verify, timeout=timeout)
        log_text = "name：%s，url：%s，body：%s，reponse：%s" % (name, url, formdata,result.status_code)
        MyLog.info(log_text)
        result_dict = eval(result.text)
        MyReplace.extract_data(result_dict, is_replace)
        # MyRemind.response_info(result_dict)
        return result


    @exception_utils
    def get_formdata(self, data):
        data = MyReplace.replace_case_with_re(data)
        sign = hashlib.md5((MyGlobal.getToken() + data).encode("utf-8")).hexdigest()
        MyGlobal.setSign(sign)
        formdata = {
            "sid": MyGlobal.getLoginSid(),
            "sign": MyGlobal.getSign(),
            "data": data
        }
        return formdata


    def merge_list_dict(self,list_dict1,list_dict2):
        new_list_dict=[]
        for i in range(len(list_dict1)):
            list_dict1[i] |= list_dict2[i]
            new_list_dict.append(list_dict1[i])
        return new_list_dict






