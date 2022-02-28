import os


# os.path.join()拼接路径
path4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.py')
a=os.path.abspath(__file__)
dd=os.path.realpath(__file__)

b=os.path.dirname

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c=os.path.dirname(os.path.abspath(__file__))

conf_dir = os.path.join(basedir, "Conf")
# print(os.path.dirname)

# print(basedir)
# print(a)
# print(c)
print(dd)


# 拼接  测试数据路径
testdata_dir = os.path.join(basedir, "DATA")
# print(testdata_dir)

# 日志路径
log_dir = os.path.join(basedir, "outputs", "logs")

# 报告路径
report_dir = os.path.join(basedir, "outputs", "reports")

log_path = os.path.join(log_dir,"api.log")

