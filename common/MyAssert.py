#coding=utf-8

import jsonpath
import ast
from common.BaseApi import BaseApi
from common.mymysql import MyMysql
from common.MyException import exception_utils

class MyAssert(BaseApi):
    """
[
{
"expr":"$..phone",
"expected":"#phone#",
"type":"eq"
},
{
"expr":"$..phone",
"expected":"#phone#",
"type":"eq"
}
]
"""
    @exception_utils
    def assert_expect(self,id,expect,actual,response_dict):
        """调用的时候先传入表格列表字段预期结果的数据，再传入返回结果的字典"""
        if expect==None:
            print("预期为None，没有执行断言~")
            return False
        else:
            try:
                print('info:用例 id "{}"'.format(id))
                expect_list = ast.literal_eval(expect)
                actual_list = ast.literal_eval(actual)
                assert_list=self.merge_list_dict(expect_list,actual_list)
                for index,check in enumerate(assert_list):
                    actual = jsonpath.jsonpath(response_dict, check["expr"])
                    if self.assert_all(actual,check):
                        print(f'info:第{index+1}次断言结果为 "{self.assert_all(actual,check)}"')
                        if index==len(expect_list)-1:
                            return True
                        else:
                            continue
                    else:
                        return False
            except:
                print("上传文件不合法,请检查expect与actual的数据格式")


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

