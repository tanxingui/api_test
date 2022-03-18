import traceback
from functools import wraps
from common.BaseRemind import Remind
Remind=Remind()
def exception_utils(func):
    """处理异常的装饰器"""
    @wraps(func)
    def wraped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #e, traceback.extract_stack()
            data=e, traceback.extract_stack()
            Remind.ex_error(data)

    return wraped
