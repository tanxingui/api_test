from enum import Enum
class Request(Enum):
    """常量存放地"""
    post = 1
    get = 2


print(Request.post.value)