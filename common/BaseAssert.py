#coding=utf-8

import jsonpath
import ast
from common.BaseApi import BaseApi
from common.mymysql import MyMysql
from common.MyException import exception_utils
from common.MyExcel_ import ExcelUtil
from common.BaseDriver import BaseDriver
from config.mypath import *
from common.BaseLog import LogUtil
MyLog=LogUtil()
MyDriver=BaseDriver()
class MyAssert(BaseApi):
    """[{
        "actual":{
            "url":"/iyourcar_autobuy/backend/apollo/user_order/list",
            "expr":"$.result.list[0].status",
            "get_type":"text"
        },
        "expected":"[2]",
        "type":"eq"
    }]"""

    @exception_utils
    def assert_expect(self, assert_list):
        """调用的时候先传入表格列表字段预期结果的数据，再传入返回结果的字典"""
        if assert_list == []:
            print("预期为None，没有执行断言~")
            return False
        else:
            assert_list=ast.literal_eval(assert_list)
            for index, assert_dict in enumerate(assert_list):
                log_text2 = "开始断言~"
                MyLog.info(log_text2)
                response_json = self.json_source(assert_dict)  # 因为公共驱动是列表的参数
                assert_result = self.assert_all(response_json, assert_dict)
                if assert_result:
                    if index == len(assert_list) - 1:
                        return True
                    else:
                        continue
                else:
                    return False

    def json_source(self,assert_dict):
        if assert_dict["actual"]["data_sources"] == "last_request":
            response_json=self.get_last_result_json()
        else:
            response_json = self.assert_request(assert_dict["actual"]["data_sources"],assert_dict["actual"]["body_key"])

        return response_json


    def assert_all(self,response_json,assert_dict):
        """alone assert"""
        "元素在元素中 返回True与False"
        actual=jsonpath.jsonpath(response_json, assert_dict["actual"]["expr"]) #actual逻辑处理
        log_text3 = "assert_type:%s，actual:%s，expected:%s" % (assert_dict["type"],actual,assert_dict["expected"])
        MyLog.info(log_text3)
        if assert_dict["type"] == "eq":  #断言逻辑处理
            return assert_dict["expected"] == actual

        elif assert_dict["type"] == "in":
            return assert_dict["expected"] in actual

        elif assert_dict["type"] == "sum":
            return assert_dict["expected"] == sum(actual)

        else:
            print("type类型错误~")
            return False

    def assert_request(self,url,body_key):

        common_value = ExcelUtil(excel_dir + "/common.xlsx").read_common()
        check_api=MyDriver.url_driver(url,body_key,common_value)
        result=self.request_api(
                name=check_api["name"],
                url=base_url+check_api["url"],
                method=check_api["method"],
                data=check_api["body"],
                is_replace=check_api["is_replace"]
            )
        return result.json()


    def assert_db(self,expect):
        """等待完善"""
        check_list = ast.literal_eval(expect)  # 1比eval安全一点。转成列表。
        db = MyMysql()
        for check in check_list:
            # 根据type来调用不同的方法来执行sql语句。
            actual=db.checkout_sql(check)
            if self.assert_all(actual, check):
                continue
            else:
                return False

