import logging
import logging.handlers
import os
import time
from common.text_util import base_dir


class LogUtil(object):
    instance = None
    init_flag = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):

        # 1、判断是否为 True，因为是实例方法，所以调用类属性要通过类对象
        if LogUtil.init_flag:
            # 2、如果 True，直接跳过不执行后续初始化动作
            return
        LogUtil.init_flag = True


        self.logger = logging.getLogger("")
        # 创建文件目录
        logs_dir = "%s/log/logs" % base_dir
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y%m%d", time.localtime())
        logfilename = '%sOkayProject.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.INFO)


    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
# 添加日志
# name="卢志豪"
# url="http：//"
# rep={"data":""}
# log_text = "name：%s，url：%s，reponse：%s" % (name, url, rep)
# LogUtil().info(log_text)