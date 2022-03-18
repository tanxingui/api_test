
<<<<<<< HEAD

from case.test_api import *
=======
>>>>>>> dev/dev-220228

if __name__ == '__main__':
    t1=Test_api()
    t1.test_api_01()
    path = "case/test_api.py"
    args = ["-v", "./" + path]
    pytest.main(args)

