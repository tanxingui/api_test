from flask import Flask, views, render_template

app = Flask(__name__)


class BaseView(views.View):
    # 如果子类忘记定义 get_template 就会报错
    def get_template(self):
        raise NotImplementedError()

    # 如果子类忘记定义 get_data 就会报错
    def get_data(self):
        raise NotImplementedError()

    def dispatch_request(self):
        # 获取模板需要的数据
        data = self.get_data()
        # 获取模板文件路径
        template = self.get_template()
        # 渲染模板文件
        return render_template(template, **data)
