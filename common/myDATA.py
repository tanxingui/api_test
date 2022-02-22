class DATA:
    """瓜瓜用来放全局变量的类"""

    pass
from common.myDATA import DATA
b=DATA()
setattr(b,'d',3)
getattr(b,"d")

