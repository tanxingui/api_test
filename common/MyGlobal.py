
"""全局变量"""
class Global:
    __GlobalSid=None
    __GlobalToken=None
    def getSid(self):
        return self.__GlobalSid
    def setSid(self,sid):
        self.__GlobalSid=sid
    def getToken(self):
        return self.__GlobalToken
    def setToken(self,token):
        self.__GlobalToken=token

# b=DATA()
# setattr(b,'d',3)
# getattr(b,"d")