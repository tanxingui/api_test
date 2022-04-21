from common.BaseApi import BaseApi
from common.BaseAssert import MyAssert
from checkout.BaseRemind import Remind
from config.mypath import *
from common.BaseLog import LogUtil
MyRemind=Remind()
MyAssert=MyAssert()
MyLog=LogUtil()
class Request(BaseApi):
    """请求、断言、写入结果"""
    """is_replace:[{"is_extract":1,"extract_expr":"$.result.list[0].order_no","rely":"10_parent_order_no"}]"""
    """is_replace:[{"is_extract":0,"rely_list":["10_parent_order_no"]}]"""
    def case_manage(self,case_name,request_list,assert_list):
        """"""
        print("\n")
        log_text1 = "case_name:%s，开始自动化运行接口用例~" % (case_name)
        MyLog.info(log_text1)
        for index,i in enumerate(request_list):
            result=self.request_api(
                name=i["name"],
                url=base_url+i["url"],
                method=i["method"],
                data=i["body"],
                is_replace=i["is_replace"]
            )
            if index+1==len(request_list):
                self.set_last_result_json(result.json()) #操作set方法设置的对象属性

        assertion = MyAssert.assert_expect(assert_list)

        return assertion








        # if assertion:
        #     # 将运行结果写入txt文件保存
        #     write_txt(text_file=run_result_txt, data=str(f"用例id__{url}__pass|"))  # 用"__"符号间隔
        # else:
        #     write_txt(text_file=run_result_txt, data=str(f"用例id__{url}__fail|"))




