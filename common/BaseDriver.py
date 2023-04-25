import ast
import re
import queue
import json
from common.MyException import *
request_queue = queue.Queue()
class BaseDriver:
    def __init__(self):
        self.request_template = """{"name":"","url":"","method":"","body":"","is_replace":""}"""

    @exception_utils
    def url_driver(self,url,body_key,common_dict):
        """common_dict=[{"url":{dict}}]"""

        template_str = self.request_template
        template_objct=ast.literal_eval(template_str)

        common_result=common_dict[url]
        is_replace_list = ast.literal_eval(common_result["is_replace"])
        for replace_list_index, data in enumerate(is_replace_list):
            if data.__contains__("rely_list"):
                for j in data["rely_list"]:
                    url = re.findall(r'(.+?)__', j["url"])
                    common_result_rely = common_dict[url[0]]
                    request_rely_body=self.body_enum(common_result_rely,j["body_key"])
                    template = template_objct.copy()
                    template['name'] = common_result_rely["api_name"]
                    template['url'] = common_result_rely["url"]
                    template['method'] = common_result_rely["method"]
                    template['body'] = request_rely_body
                    template['is_replace'] = common_result_rely["is_replace"]
                    request_queue.put(template)

        template = template_objct.copy()
        request_body=self.body_enum(common_result,body_key)
        template['name'] = common_result["api_name"]
        template['url'] = common_result["url"]
        template['method'] = common_result["method"]
        template['body'] = request_body
        template['is_replace'] = common_result["is_replace"]
        request_queue.put(template)
        return template

    @exception_utils
    def url_list_driver(self,url_list,step,common_dict):
        request_list = []
        body_key_list = step.split(r",")
        for index, url in enumerate(url_list):
            body_key=re.findall(r"（#(.*?)）",body_key_list[index])
            if body_key==[]:
                print("用例的step没有定位到__(.*?)__的值")
                raise
            self.url_driver(url,body_key[0],common_dict)

        for p in range(request_queue.qsize()):
            request_list.append(request_queue.get())
        return request_list

    @exception_utils
    def body_enum(self,common_result,body_key):
        body_dict=ast.literal_eval(common_result["body"])
        # key_list = re.findall(r'&(.+?),', step)
        if body_dict.keys().__contains__(body_key):
            return json.dumps(body_dict[body_key],ensure_ascii=False)#使用dumps可以保留双引号
        else:
            print("操作步骤没有包含该url的key值")
            raise









