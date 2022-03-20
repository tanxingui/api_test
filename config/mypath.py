import os


basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path_dir = os.path.join(basedir, "config")

# 拼接  测试数据路径
testdata_dir = os.path.join(basedir, "data")

# 日志路径
log_dir = os.path.join(basedir, "log", "logs")

# 报告路径
report_dir = os.path.join(basedir, "report", "result")

log_path = os.path.join(log_dir,"api.log")

