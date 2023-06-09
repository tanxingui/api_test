import jsonpath
import ast
import re
from common.MyException import exception_utils
from faker import Faker
faker=Faker()
class Replace_data():
    instance = None
    init_flag = None
    replace_dict={}
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        # 1、判断是否为 True，因为是实例方法，所以调用类属性要通过类对象
        if Replace_data.init_flag:
            # 2、如果 True，直接跳过不执行后续初始化动作
            return
        Replace_data.init_flag = True


    """目前只支持提取第一个"""
    def add_replace_dict(self,key,replace_dict):
        self.replace_dict[key]=replace_dict
    def get_replace_dict(self,key):
        return self.replace_dict[key]
    def get_random_int(self):
         pass
    def get_random_phone(self):
        return faker.phone_number()
    def get_random_name(self):
        return faker.name()
    @exception_utils
    def replace_case_with_re(self,Data):
        """{"id":"$#/iyourcar_autobuy/backend/apollo/user_order/list__id#"}"""
        if Data.count("$")==0:
            return Data
        else:
            #正则获取出一个列表，只负责拿
            rely_list = self.is_rely(Data)
            num=Data.count("$")
            index = 0
            for i in range(num):
                """随时调用字典的值"""

                if "$#phone#" in Data:
                    Data = Data.replace(f"$#phone#", f"{self.get_random_phone()}")

                elif "$#name#" in Data:
                    Data = Data.replace(f"$#name#", f"{self.get_random_name()}")

                elif f"$#{rely_list[index]}#" in Data:

                    Data=Data.replace(f"$#{rely_list[index]}#",f"{self.get_replace_dict(f'{rely_list[index]}')}")
                    #解决一个data有两个相同参数的情况
                    if index+1 < len(rely_list):
                        index += 1

                #判断是否最后一个替换
                if i + 1 == num:
                    return Data
                else:
                    continue

    @exception_utils
    def is_rely(self,data):
        sss=re.findall('#(.*?)#', data)
        return sss

    @exception_utils
    def extract_data(self,result_dict,is_replace):
        #负责装进去
        is_replace_list = ast.literal_eval(is_replace)
        for index,i in enumerate(is_replace_list):
            """判断是否需要替换"""
            if i["is_extract"] ==1:
                name=jsonpath.jsonpath(result_dict,i["extract_expr"])
                key=i["rely"]
                if type(name)==bool:
                    print(f"jsonpath表达式没有定位到{key}的数据")
                    self.add_replace_dict(key,"")
                else:
                    self.add_replace_dict(key,name[0])

    # @exception_utils
    # def set_rely_list(self,is_replace):
    #     """设置依赖url列表"""
    #     rely_list=[]
    #     is_replace_list = ast.literal_eval(is_replace)
    #     for index, dict in enumerate(is_replace_list):
    #         if dict.__contains__("rely_list"):
    #             for j in dict["rely_list"]:
    #                 rely_list.append(j["url"])
    #     return rely_list






