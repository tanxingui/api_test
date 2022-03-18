import pytest
def start_api():
    path = "case/test_api.py"
    args = ["-v", "../" + path]
    pytest.main(args)