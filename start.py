
from case.test_api import *

if __name__ == '__main__':
    path = "case/test_api.py"
    args = ["-v", "./" + path]
    pytest.main(args)
