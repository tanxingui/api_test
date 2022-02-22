
from configparser import ConfigParser
#瓜瓜读取配置文件封装

class MyConf(ConfigParser):

    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")