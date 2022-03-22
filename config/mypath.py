import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_dir = os.path.join(base_dir, "config")
# url域名
host="https://api.s.youcheyihou.com"
environment="testapi"
base_url=os.path.join(host,environment)
# 拼接  测试数据路径
testdata_dir = os.path.join(base_dir, "data")
excel_dir=os.path.join(testdata_dir,"excel_case")
"""运行模块下的全部yaml"""
yaml_dir=os.path.join(testdata_dir,"yaml_case")

# 日志路径
log_dir = os.path.join(base_dir, "log", "logs")

# 报告路径
report_dir = os.path.join(base_dir, "report", "result")

log_path = os.path.join(log_dir,"api.log")

