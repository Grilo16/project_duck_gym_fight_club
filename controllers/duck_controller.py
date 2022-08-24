from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request

from models.duck import Duck

from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import new_duck

from repositories.ducks_in_classes_repository import get_classes_from_duck
from repositories.ducks_in_classes_repository import get_classes_not_enroled_by_duck

duck_pictures = ['rdbp-gallery-1.png', 'rdbp-gallery-2.png', 'rdbp-gallery-3.png', 'rdbp-gallery-4.png', 'rdbp-gallery-5.png', 'rdbp-gallery-6.png', 'rdbp-gallery-7.png', 'rdbp-gallery-8.png', 'rdbp-gallery-9.png', 'rdbp-gallery-10.png', 'rdbp-gallery-11.png', 'rdbp-gallery-12.png', 'rdbp-gallery-13.png', 'rdbp-gallery-14.png', 'rdbp-gallery-15.png', 'rdbp-gallery-16.png', 'rdbp-gallery-17.png', 'rdbp-gallery-18.png', 'rdbp-gallery-19.png', 'rdbp-gallery-20.png']


duck_blueprint = Blueprint("ducks", __name__)

@duck_blueprint.route("/all_ducks")
def show_ducks():
    all_ducks = get_all_ducks()
    return render_template("ducks/show_ducks.html", all_ducks = all_ducks)

@duck_blueprint.route("/duck_stats/<duck_id>")
def show_duck_stats(duck_id):
    duck = select_duck_by_id(duck_id)
    print(duck.image)
    duck_classes = get_classes_from_duck(duck)
    duck_not_in_classes = get_classes_not_enroled_by_duck(duck)
    return render_template("ducks/view_duck_stats.html", duck = duck, duck_classes = duck_classes, duck_not_in_classes=duck_not_in_classes)
    
@duck_blueprint.route("/create_duck", methods = ["GET"])
def create_duck_page():
    return render_template("ducks/create_duck.html", duck_pictures = duck_pictures)

@duck_blueprint.route("/create_duck", methods = ["POST"])
def save_new_duck():
    new_duck(Duck(request.form["duck_name"], 0, 0, 0, 100, image = request.form["duck_image"]))
    return redirect("/all_ducks")

@duck_blueprint.route("/test")
def stek():
    duck1 = select_duck_by_id(2)
    duck2 = select_duck_by_id(5)
    return render_template("test.html", duck1=duck1, duck2=duck2)
