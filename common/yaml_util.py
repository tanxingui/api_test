@exception
def read_yaml(yaml_file):
    """读取yaml"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        print(value)
        return value

@exception
def write_yaml(data, yaml_file):
    """写yaml"""
    with open(yaml_file, 'w') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True, sort_keys=False, default_flow_style=False)

@exception
def truncate_yaml(yaml_file):
    """清空yaml"""
    with open(yaml_file, 'w') as f:
        f.truncate()

@exception
def handler():
    """根据读取excel数据，生成yaml的测试用例数据"""
    file = "%s/data/case_excel/接口测试框架实践用例.xlsx" % base_dir
    value = ExcelUtil(file).read_excel()
    sheet_names = ExcelUtil(file).wb.sheetnames
    n = 0
    for sheet in sheet_names:
        data = value[n]
        file = '%s/data/case_yaml/%s.yaml' % (base_dir, sheet)
        write_yaml(data=data, yaml_file=file)
        n += 1
