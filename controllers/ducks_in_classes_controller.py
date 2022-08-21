from flask import render_template
from flask import redirect
from flask import request
from flask import Blueprint
from db.run_sql import run_sql

from repositories.duck_repository import select_duck_by_id


from repositories.gym_class_repository import select_class_by_id

from repositories.ducks_in_classes_repository import add_duck_to_class
from repositories.ducks_in_classes_repository import get_ducks_in_class
from repositories.ducks_in_classes_repository import remove_duck_from_class

ducks_in_classes_blueprint = Blueprint("ducks_in_classes", __name__)

@ducks_in_classes_blueprint.route("/gym_class/ducks_in_class/<gc_id>")
def show_ducks_in_class(gc_id):
    gym_class = select_class_by_id(gc_id)
    ducks_in_class = get_ducks_in_class(gym_class)
    return render_template("ducks_in_classes/ducks_in_class.html", gym_class = gym_class, ducks_in_class=ducks_in_class)

@ducks_in_classes_blueprint.route("/add/duck_to_class", methods = ["POST"])
def add_duck_to_class_post():
    duck = select_duck_by_id(request.form["ducks"])
    gym_class = select_class_by_id(request.form["class"])
    add_duck_to_class(duck, gym_class)
    return redirect("/")
    
@ducks_in_classes_blueprint.route("/duck/<duck_id>/finish_class/<gc_id>", methods=["POST"])
def remove_duck_from_class_post(duck_id, gc_id):
    duck = select_duck_by_id(duck_id)
    gym_class = select_class_by_id(gc_id)
    remove_duck_from_class(duck, gym_class)
    return redirect(f"/gym_class/ducks_in_class/{gc_id}")
