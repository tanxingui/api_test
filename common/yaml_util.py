from config.mypath import *
from common.MyExcel_ import ExcelUtil
from common.MyException import *
import yaml
@exception_utils
def read_yaml(yaml_file):
    """读取yaml"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        print(value)
        return value

@exception_utils
def write_yaml(data, yaml_file):
    """写yaml"""
    with open(yaml_file, 'w') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True, sort_keys=False, default_flow_style=False)

@exception_utils
def truncate_yaml(yaml_file):
    """清空yaml"""
    with open(yaml_file, 'w') as f:
        f.truncate()

@exception_utils
def handler(excel_name):
    """根据读取excel数据，生成yaml的测试用例数据"""
    path = f"{yaml_dir}/{excel_name}"
    if not os.path.exists(path):
        os.mkdir(path)
    file = os.path.join(excel_dir,excel_name)
    value = ExcelUtil(file).read_excel()
    sheet_names = ExcelUtil(file).wb.sheetnames
    n = 0
    for sheet in sheet_names:
        data = value[n]
        file = '%s/%s.yaml' % (f"{yaml_dir}/{excel_name}",sheet)
        write_yaml(data=data, yaml_file=file)
        n += 1
@exception_utils
def merge_yaml():
    """合并全部用例一起执行"""
    excel=[]
    data_list=os.listdir(yaml_dir)
    for index,data in enumerate(data_list[1:]):
        work_dir=yaml_dir+"/"+data
        dir_list = os.listdir(work_dir)
        for i in dir_list:
            yaml_file = os.path.join(work_dir, i)
            for j in read_yaml(yaml_file)["cases"]:
                excel.append(j)
    return excel