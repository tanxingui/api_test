# 导入 Flask 和 蓝图 Blueprint
from flask import Flask
# 导入蓝图类
from demo_flask.Controller.NewsController import NewsController
# from Controller.ProductsController import ProductsController
app = Flask(__name__)


# from demo.flask.demo2.userview import UserView
# app.add_url_rule('/user/', view_func=UserView.as_view('UserView'))
# 注册蓝图
app.register_blueprint(NewsController.blueprint)
# app.register_blueprint(ProductsController.blueprint)

if __name__ == '__main__':
    app.run(debug=True,port=7777,host='0.0.0.0')