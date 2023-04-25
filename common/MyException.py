import traceback
from functools import wraps
from checkout.BaseRemind import Remind
Remind=Remind()
def exception_utils(func):
    """处理异常的装饰器"""
    @wraps(func)    # wraps函数是为了解决函数使用装饰器修饰时丢失本身的一些属性而出现的
    def wraped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #e, traceback.extract_stack()
            data=e, traceback.extract_stack()
            Remind.ex_error(data)

    return wraped
