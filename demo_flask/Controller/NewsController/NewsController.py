# 导入蓝图
from flask import Blueprint, render_template,request
from common.BaseRemind import Remind
from config.myconf import MyConf
import pytest
def start_api():
    path = "case/test_api.py"
    args = ["-v", "../" + path]
    pytest.main(args)
MyConf_2b=MyConf()
MyRemind=Remind()
"""
实例化蓝图对象
第一个参数：蓝图名称
第二个参数：导入蓝图的名称
第三个参数：蓝图前缀，该蓝图下的路由规则前缀都需要加上这个
"""
blueprint = Blueprint('NewsController', __name__, url_prefix="/new", template_folder="templates",static_folder="static")
#static_folder="static"
# 用蓝图注册路由

@blueprint.route("/2b/",methods=["POST"])
def society_news():
    """1:新建单辆车 2："""
    if request.form["type"]=='1':
        data="/单个订单待付款"
        MyConf_2b.setConf(data+".xlsx")
        #MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    elif request.form["type"]=='2':
        data = "/单个订单待提车"
        MyConf_2b.setConf(data+".xlsx")
        # MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    elif request.form["type"]=='3':
        data = "/整版订单待付款"
        MyConf_2b.setConf(data+".xlsx")
        # MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    elif request.form["type"]=='4':
        data = "/整版订单待提车"
        MyConf_2b.setConf(data+".xlsx")
        # MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    elif request.form["type"]=='5':
        data = "/待审核的审核单"
        MyConf_2b.setConf(data+".xlsx")
        # MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    elif request.form["type"]=='6':
        data = "/采购完成的采购单"
        MyConf_2b.setConf(data+".xlsx")
        # MyConf_2b.setConf(data+".xlsx")
        start_api()
        return MyRemind.param_ok(data)
    else:
        return MyRemind.param_error()

@blueprint.route("/order/")
def tech_news():
    name="B端订单卢志豪测试"
    return render_template('society.html',name=name)
