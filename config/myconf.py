
# from configparser import ConfigParser
#读取配置文件封装

class MyConf():
    conf=""
    instance = None
    init_flag = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        # 1、判断是否为 True，因为是实例方法，所以调用类属性要通过类对象
        if MyConf.init_flag:
            # 2、如果 True，直接跳过不执行后续初始化动作
            return
        MyConf.init_flag = True
    def setConf(self,path):
        self.conf=path
    def getConf(self):
        return self.conf