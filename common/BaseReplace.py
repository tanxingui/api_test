import jsonpath
import ast

class Replace_data():
    instance = None
    init_flag = None
    name={}
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
    def add_name(self,key,name):
        self.name[key]=name
    def get_name(self,key):
        return self.name[key]
    def replace_case_with_re(self, id,Data):
        """{"id":"$#15_0#","name":"$#15_1#"}"""
        if Data.count("$")==0:
            return Data
        else:
            num=Data.count("$")
            for i in range(num):
                """id-1 只适配上一个接口就为目标接口的情况"""
                if f"$#{id-1}_{i}#" in Data:
                    Data=Data.replace(f"$#{id-1}_{i}#",f"{self.get_name(f'{id-1}_{i}')}")
                    if i+1==num:
                        return Data
                    else:
                        continue
                else:
                    print(f"id{id}替换表达式的格式错误~")
                    raise

    def extract_data(self,id,expect,result_dict):
        expect_list = ast.literal_eval(expect)

        for index,i in enumerate(expect_list):
            """判断是否需要替换"""
            if i["is_extract"] ==1:
                name=jsonpath.jsonpath(result_dict,i["extract_expr"])
                self.add_name(str(id)+"_"+str(index),name[0])

            else:
                pass




