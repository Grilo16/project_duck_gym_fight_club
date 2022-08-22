from flask import Blueprint
from flask import redirect
from flask import request

from repositories.duck_repository import select_duck_by_id

from repositories.gym_class_repository import select_class_by_id

from repositories.ducks_in_classes_repository import add_duck_to_class
from repositories.ducks_in_classes_repository import remove_duck_from_class

ducks_in_classes_blueprint = Blueprint("ducks_in_classes", __name__)

@ducks_in_classes_blueprint.route("/add/duck_to_class", methods = ["POST"])
def add_duck_to_class_post():
    duck = select_duck_by_id(request.form["duck_id"])
    gym_class = select_class_by_id(request.form["gym_class_id"])
    add_duck_to_class(duck, gym_class)
    return redirect(f"/{request.form['origin']}")
    
@ducks_in_classes_blueprint.route("/duck/finish_class", methods=["POST"])
def remove_duck_from_class_post():
    duck = select_duck_by_id(request.form["duck_id"])
    gym_class = select_class_by_id(request.form["class_id"])
    remove_duck_from_class(duck, gym_class)
    return redirect(f"/{request.form['origin']}")
    