from flask import render_template
from flask import redirect
from flask import request
from flask import Blueprint
from db.run_sql import run_sql

from repositories.duck_repository import select_duck_by_id


from repositories.gym_class_repository import select_class_by_id

from repositories.ducks_in_classes_repository import add_duck_to_class
from repositories.ducks_in_classes_repository import get_classes_from_duck
from repositories.ducks_in_classes_repository import get_ducks_in_class
from repositories.ducks_in_classes_repository import remove_duck_from_class

ducks_in_classes_blueprint = Blueprint("ducks_in_classes", __name__)

@ducks_in_classes_blueprint.route("/add/duck_to_class", methods = ["POST"])
def add_duck_to_class_post():
    duck = select_duck_by_id(request.form["ducks"])
    gym_class = select_class_by_id(request.form["class"])
    add_duck_to_class(duck, gym_class)
    return redirect("/")
    
@ducks_in_classes_blueprint.route("/duck/finish_class", methods=["POST"])
def remove_duck_from_class_post():
    origin = request.form["origin"]
    duck = select_duck_by_id(request.form["duck_id"])
    gym_class = select_class_by_id(request.form["class_id"])
    remove_duck_from_class(duck, gym_class)
    return redirect("/"+request.form["origin"])
    # return redirect(f"/gym_class/ducks_in_class/{request.form['class_id']}")

# Obsolete now showing on the duck stat page


# @ducks_in_classes_blueprint.route("/duck/<duck_id>/classes")
# def show_classes_from_duck(duck_id):
#     duck = select_duck_by_id(duck_id)
#     duck_gym_classes = get_classes_from_duck(duck)
#     return render_template("ducks_in_classes/classes_from_duck.html", duck_gym_classes = duck_gym_classes, duck=duck)


# Obsolete cause values are now within the class page

# @ducks_in_classes_blueprint.route("/gym_class/ducks_in_class/<gc_id>")
# def show_ducks_in_class(gc_id):
#     gym_class = select_class_by_id(gc_id)
#     ducks_in_class = get_ducks_in_class(gym_class)
#     return render_template("ducks_in_classes/ducks_in_class.html", gym_class = gym_class, ducks_in_class=ducks_in_class)
