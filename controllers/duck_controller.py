from flask import Blueprint
from flask import render_template

duck_blueprint = Blueprint("ducks", __name__)


@duck_blueprint.route("/all_ducks")
def show_ducks():
    return render_template("ducks/show_ducks.html")
