from flask import Blueprint
from flask import render_template

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route("/all_classes")
def show_classes():
    return render_template("classes/show_classes.html")