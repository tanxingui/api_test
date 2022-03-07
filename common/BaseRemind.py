"""提示类"""
import jsonpath
class Remind:

    def Exception_class(self,key_list, data):
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
        elif data[10] != None and type(data[10]) != str:
            self.format_error(key_list[10], str)
            raise

    def format_error(self,key, type):
        print(f"{key}值为空或者数据格式不是{type}")
    def response_info(self,id,dict):
        print(f"用例id为{id:->15}")
        print(f'errcode:{jsonpath.jsonpath(dict, "$..errcode")[0]}')
