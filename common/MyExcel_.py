from openpyxl import Workbook,load_workbook
from common.MyException import exception_utils
from common.BaseApi import BaseApi

@exception_utils
class ExcelUtil(BaseApi):
    """封装操作excel的方法，主要作用2个：
1、用于数据处理，读取excel中用例后返回规定的字典，便于生成yaml
2、将运行结果数据存入excel中对应列
"""

    def __init__(self, excel_path):
        self.wb = load_workbook(excel_path)
        self.template = """{"id":0,"url":"","case_name":"","header":"","method":"","body":"",
        "expect":"","actual":"","valiadate":""},"""  # 这个是写入用例的模板

    @exception_utils
    def read_excel(self):
        """读取excel，处理数据，并返回一个格式处理后的字典"""
        value = []
        for sheetname in self.wb.sheetnames:
            ws = self.wb[sheetname]
            case_list_3 = list(ws.values)
            """# 志豪获得id为空的case的索引
               # 新列表的概念
               # 志豪取前10位成一个新列表
            """
            case_list_3.pop(0)  # 去掉表头
            # 处理行id为空的值
            bbb = [i for i, case in enumerate(case_list_3) if case[0] == None]
            case_list_2 = [v for i, v in enumerate(case_list_3) if i not in bbb]
            # 处理列超过10的空值
            case_list_4 = [case[:9] for case in case_list_2 if len(case) > 10]
            del case_list_3
            del case_list_2
            cases_num = len(case_list_4) # 一个sheet中用例的数量

            cases_template = self.template * cases_num
            cases_template_list = eval("[" + cases_template[:-1] + "]")   # 与用例相同长度的模板
            case_list=self.format_cases(case_list_4)

            for i in range(len(case_list)):  # i：第i个用例
                # 每个用例中字段是9个，因此这样写
                cases_template_list[i]['id'] = case_list[i][0]
                cases_template_list[i]['url'] = case_list[i][1]
                cases_template_list[i]['case_name'] = case_list[i][2]
                cases_template_list[i]['header'] = case_list[i][3]
                cases_template_list[i]['method'] = case_list[i][4]
                cases_template_list[i]['body'] = case_list[i][5]
                cases_template_list[i]['expect'] = case_list[i][6]
                cases_template_list[i]['actual'] = case_list[i][7]
                cases_template_list[i]['valiadate'] = case_list[i][8]

            value.append({"cases": cases_template_list})


        return value

    @exception_utils
    def write_excel(self):
        """运行结果写入excel"""
        l_reponse, l_ispass = read_txt_handel()
        print(l_reponse.__len__())
        print(l_ispass.__len__())

        i = 0
        j = 0
        for sheetname in self.wb.sheetnames:
            ws = self.wb[sheetname]
            # 实际结果列
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=8, min_col=8):
                for cell in row:
                    cell.value = l_reponse[i]
                    # print("resp:%s" % i, cell.value)
                    i += 1
            # 是否通过列
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=9, min_col=9):
                for cell in row:
                    cell.value = l_ispass[j]
                    # print("ispass%s:" % j, cell.value)
                    j += 1

        save_path = "%s/output/run_result_excel/运行结果_%s.xlsx" % (self.base_dir, time.strftime("%Y%m%d_%H:%M:%S"))
        self.wb.save(save_path)

