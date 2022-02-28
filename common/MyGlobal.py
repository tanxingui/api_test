
"""全局变量"""
class Global:
    __GlobalSid=None
    __GlobalToken=None
    __GlobalSign=None
    instance = None
    init_flag = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        # 1、判断是否为 True，因为是实例方法，所以调用类属性要通过类对象
        if Global.init_flag:
            # 2、如果 True，直接跳过不执行后续初始化动作
            return
        Global.init_flag = True
    def getLoginSid(self):
        return self.__GlobalSid
    def setLoginSid(self,sid):
        self.__GlobalSid=sid
    def getToken(self):
        return self.__GlobalToken
    def setToken(self,token):
        self.__GlobalToken=token
    def getSign(self):
        return self.__GlobalSign
    def setSign(self,sign):
        self.__GlobalSign=sign




# b=DATA()
# setattr(b,'d',3)
# getattr(b,"d")