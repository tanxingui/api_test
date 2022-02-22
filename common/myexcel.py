
from openpyxl import load_workbook

class Myexcel:

    def __init__(self,path,name):
        wb=load_workbook(path)
        self.sh=wb[name]

    # 封装拿excel的数据
    def read_excel(self):
        all_data = []
        data = list(self.sh.values)
        keys = data[0]  # 获取所有的列名
        for row in data[1:]:
            row_dict = dict(zip(keys, row))
            all_data.append(row_dict)
        return all_data
