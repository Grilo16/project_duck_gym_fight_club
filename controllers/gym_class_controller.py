from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request

from repositories.ducks_in_classes_repository import get_ducks_in_class 
from repositories.ducks_in_classes_repository import get_ducks_not_enrolled_in_class

from repositories.gym_class_repository import get_all_classes
from repositories.gym_class_repository import select_class_by_id
from repositories.gym_class_repository import new_gym_class_for_duckies

from models.gym_class import Gym_class

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route("/all_classes")
def show_classes():
    all_classes = get_all_classes()
    return render_template("classes/show_classes.html", all_classes=all_classes)

@gym_class_blueprint.route("/gym_class/<id>")
def view_class_info(id):
    gym_class = select_class_by_id(id)
    ducks_in_class = get_ducks_in_class(gym_class)
    ducks_not_enroled = get_ducks_not_enrolled_in_class(gym_class)
    return render_template("classes/show_class_info.html", gym_class=gym_class, ducks_in_class = ducks_in_class, ducks_not_enroled=ducks_not_enroled)

@gym_class_blueprint.route("/create_class", methods=["GET"])
def create_new_gym_class_form():
    return render_template("classes/create_class.html")

@gym_class_blueprint.route("/create_class", methods=["POST"])
def create_new_gym_class():
    new_gym_class_for_duckies(Gym_class(**request.form))
    return redirect("/all_classes")