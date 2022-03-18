from flask import Blueprint,render_template

blueprint = Blueprint("ProductsController", __name__, url_prefix="/product", template_folder="templates",static_folder="static")


@blueprint.route("/car")
def car_products():
    return render_template('society1.html')


@blueprint.route("/baby")
def baby_products():
    return "婴儿产品版块"