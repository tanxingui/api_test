"""提示类 格式校验类"""
import jsonpath
import re

class Remind:
    def Excel_manage(self,case_list):
        """{"case_name":"","precondition":"","step":"",
                "request_list":"","assert":""},"""
        "校验"
        excel_format_list=self.format_excel_list(case_list)
        # 取excel前十一位的值 *
        case_list_5 = [case[:5] for case in excel_format_list]
        self.Excel_Checker(case_list_5)
        case_format_list=self.format_case_list(case_list_5)

        return case_format_list

    def Common_Excel_manage(self,case_list):
        """{"id":0,"url":"","api_name":"","method":"","body":"","is_replace":""},"""
        "校验"
        excel_format_list = self.format_excel_list(case_list)
        # 取excel前六位的值 *
        case_list_6 = [case[:6] for case in excel_format_list]
        self.Common_Excel_Checker(case_list_6)
        case_format_list = self.format_common_case_list(case_list_6)
        return case_format_list

    def Excel_Checker(self,case_list):
        """校验器"""
        key_list = ["case_name", "precondition", "step", "request_list", "assert"]
        for index, data in enumerate(case_list):  # 遍历caselist的枚举和值
            #type(data[2]) != str or data[2] == None
            if type(data[0]) != str or data[0] == None:
                self.format_error(key_list[0], int)
                raise
            elif data[1] != None and type(data[1]) != str:
                self.format_error(key_list[1], str)
                raise
            elif type(data[2]) != str or data[2] == None:
                self.format_error(key_list[2], str)
                raise
            elif type(data[3]) != str or data[3] == None:
                self.format_error(key_list[3], str)
                raise
            elif data[4] != None and type(data[4]) != str:
                self.format_error(key_list[4], str)
                raise

    def Common_Excel_Checker(self,case_list):
        """校验器"""
        key_list = ["id", "url", "api_name", "method", "body", "is_replace"]
        for index, data in enumerate(case_list):
            if type(data[0]) != int or data[0] == None:
                self.format_error(key_list[0], int)
                raise
            elif type(data[1]) != str or data[1] == None:
                self.format_error(key_list[1], str)
                raise
            elif type(data[2]) != str or data[2] == None:
                self.format_error(key_list[2], str)
                raise
            elif type(data[3]) != str or data[3] == None:
                self.format_error(key_list[3], str)
                raise
            elif data[4] != None and type(data[4]) != str:
                self.format_error(key_list[4], str)
                raise
            elif data[5] != None and type(data[5]) != str:
                self.format_error(key_list[5], str)
                raise
    def format_case_list(self, case_list):
        """# 获得id为空的case的索引
           # 新列表的概念
           # 取前11位成一个新列表
        """
        for case_index, tuple_data in enumerate(case_list):
            str_list = list(tuple_data)
            for index, data in enumerate(str_list):
                if type(data) == str:
                    mm = data.replace("\n", "").replace(" ", "").replace("，",",").replace("(","（").replace(")","）")
                    str_list[index] = mm
            case_list[case_index]=tuple(str_list)
        return case_list
    def format_common_case_list(self,case_list):
        for case_index, tuple_data in enumerate(case_list):
            str_list = list(tuple_data)
            for index, data in enumerate(str_list):
                if type(data) == str:
                    mm = data.replace("\n", "").replace(" ", "").replace("，",",")
                    str_list[index] = self.format_time(mm)
            case_list[case_index]=tuple(str_list)
        return case_list

    def format_time(self,str):
        from_time = re.findall('from_time":"(.*?)"', str)
        end_time= re.findall('end_time":"(.*?)"', str)
        pay_time = re.findall('pay_time":"(.*?)"', str)
        sign_time= re.findall('sign_time":"(.*?)"', str)
        mmm=from_time+end_time+pay_time+sign_time
        if mmm==[]:
            return str
        else:
            for index, data in enumerate(mmm):
                mmm_sub = mmm[index][:10] + " " + mmm[index][10:]
                str = re.sub(mmm[index], mmm_sub, str)
            return str
    def format_excel_list(self,case_list):
        """获取到数居前的一个处理"""
        # 去掉表头
        case_list.pop(0)
        # 处理行id为空的值
        case_id_None = [i for i, case in enumerate(case_list) if case[0] == None]
        case_list_new = [v for i, v in enumerate(case_list) if i not in case_id_None]
        del case_list
        return case_list_new

    def format_error(self,key, type):
        print(f"{key}值为空或者数据格式不是{type}")
    def response_info(self,dict):
        # print(f"用例id为{id:->15}")
        print(f'errcode:{jsonpath.jsonpath(dict, "$..errcode")[0]}')
    def request_error(self,data):
        print("请检查url是否输入正确")
        print(data)
    def ex_error(self,data):
        print('出现异常，error is %s\n%s' % (data))
    def param_error(self):
        return "参数错误"

    def param_ok(self,data):
        return '你好，新贵，今天过得怎么样？已完成创建'+data+"数据"
