"""提示类 格式校验类"""
import jsonpath

class Remind:
    def Excel_manage(self,case_list):
        """{"id":0,"url":"","case_name":"","header":"","method":"","body":"",
                "expect":"","actual":"","valiadate":"","is_replace":"","is_perform":""},"""
        "校验"
        excel_format_list=self.format_excel_list(case_list)
        self.Excel_Checker(excel_format_list)
        case_format_list=self.format_case_list(excel_format_list)
        return case_format_list

    def Excel_Checker(self,case_list):
        """校验器"""
        key_list = ["id", "url", "case_name", "header", "method", "body", "expect", "actual", "valiadate","is_replace","is_perform"]
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
            elif data[3] != None and type(data[3]) != str:
                self.format_error(key_list[3], str)
                raise
            elif data[4] != None and type(data[4]) != str:
                self.format_error(key_list[4], str)
                raise
            elif data[5] != None and type(data[5]) != str:
                self.format_error(key_list[5], str)
                raise
            elif data[6] != None and type(data[6]) != str:
                self.format_error(key_list[6], str)
                raise
            elif data[7] != None and type(data[7]) != str:
                self.format_error(key_list[7], str)
                raise
            elif data[8] != None and type(data[8]) != str:
                self.format_error(key_list[8], str)
                raise
            elif data[9] != None and type(data[9]) != str:
                self.format_error(key_list[9], str)
                raise
            elif type(data[10]) != int or data[10] == None:
                self.format_error(key_list[10], str)
                raise
    def format_case_list(self, case_list):
        """# 志豪获得id为空的case的索引
           # 新列表的概念
           # 志豪取前11位成一个新列表
        """
        for case_index, tuple_data in enumerate(case_list):
            str_list = list(tuple_data)
            for index, data in enumerate(str_list):
                if type(data) == str:
                    mm = data.replace("\n", "")
                    str_list[index] = mm
            case_list[case_index]=tuple(str_list)
        return case_list
    def format_excel_list(self,case_list):
        """获取到数居前的一个处理"""
        # 去掉表头
        case_list.pop(0)
        # 处理行id为空的值
        case_id_None = [i for i, case in enumerate(case_list) if case[0] == None]
        case_list_new = [v for i, v in enumerate(case_list) if i not in case_id_None]
        # 取excel前十一位的值 *
        case_list_11 = [case[:11] for case in case_list_new if len(case) > 12]
        del case_list
        del case_list_new
        return case_list_11

    def format_error(self,key, type):
        print(f"{key}值为空或者数据格式不是{type}")
    def response_info(self,id,dict):
        print(f"用例id为{id:->15}")
        print(f'errcode:{jsonpath.jsonpath(dict, "$..errcode")[0]}')
    def request_error(self,data):
        print("请检查url是否输入正确")
        print(data)
    def ex_error(self,data):
        print('出现异常，error is %s\n%s' % (data))
    def param_error(self):
        return "参数错误"

    def param_ok(self,data):
        return '你好，志豪，今天过得怎么样？已完成创建'+data+"数据"
