#coding=utf-8

import jsonpath
import ast

from common.mymysql import MyMysql


class myassert:

    def myassert(self,check_str,response_dict):
        """调用的时候先传入表格列表字段预期结果的数据，再传入返回结果的字典"""

        check_res = []
        """判断很多个预期结果的时候的一个空列表"""
        check_list = ast.literal_eval(check_str)
        for check in check_list:
            actual = jsonpath.jsonpath(response_dict, check["expr"])
            if isinstance(actual, list):
                actual = actual[0]
            if check["type"] == "eq":
                check_res.append(actual == check["expected"])

        if False in check_res:
            return False
        else:
            return True

    def assert_db(self,check_db_str):
        check_db_res = []
        check_db_list = eval(check_db_str)  # 1比eval安全一点。转成列表。
        db = MyMysql()
        for check_db_dict in check_db_list:
            # 根据type来调用不同的方法来执行sql语句。
            if check_db_dict["type"] == "count":
                # 执行sql语句。查询结果是一个整数
                res = db.get_count(check_db_dict["sql"])
            elif check_db_dict["type"] == "eq":
                res = db.get_many_data(check_db_dict["sql"])
            else:
                raise Exception
            check_db_res.append(res == check_db_dict["expected"])
        if False in check_db_res:
            return False
        else:
            return True

