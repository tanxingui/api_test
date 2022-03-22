import pytest
import os
import time
from common.yaml_util import *
from config.mypath import *
from common.text_util import *

# tempdir_path = "report/allure/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
if __name__ == '__main__':
    handler("B端创建数据.xlsx")
    truncate_txt("%s/report/result/result.txt" % base_dir)
    path = "case/test_api.py"
    args = ["-v", "./" + path]
    pytest.main(args)

    # os.system("pytest --alluredir %s" % tempdir_path)
    # os.system("allure generate %s"
    #           " -o report/allure/allure_report --clean" % tempdir_path)
