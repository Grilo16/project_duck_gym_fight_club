from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request


from models.gym_class import Gym_class

from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import update_duck
from repositories.duck_repository import remove_duck

from repositories.gym_class_repository import get_all_classes
from repositories.gym_class_repository import remove_class
from repositories.gym_class_repository import select_class_by_id
from repositories.gym_class_repository import update_gym_class

duck_pictures = ['rdbp-gallery-1.png', 'rdbp-gallery-2.png', 'rdbp-gallery-3.png', 'rdbp-gallery-4.png', 'rdbp-gallery-5.png', 'rdbp-gallery-6.png', 'rdbp-gallery-7.png', 'rdbp-gallery-8.png', 'rdbp-gallery-9.png', 'rdbp-gallery-10.png', 'rdbp-gallery-11.png', 'rdbp-gallery-12.png', 'rdbp-gallery-13.png', 'rdbp-gallery-14.png', 'rdbp-gallery-15.png', 'rdbp-gallery-16.png', 'rdbp-gallery-17.png', 'rdbp-gallery-18.png', 'rdbp-gallery-19.png', 'rdbp-gallery-20.png', "eric.jpg"]



admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route("/admin")
def admin_page():
    all_ducks = get_all_ducks()
    all_gym_classes = get_all_classes()
    return render_template("admin/admin_page.html", all_ducks=all_ducks, all_gym_classes = all_gym_classes)

@admin_blueprint.route("/duck_stats/admin/<duck_id>", methods=["GET"])
def admin_page_edit_duck_get(duck_id):
    duck = select_duck_by_id(duck_id)
    return render_template("admin/edit_duck_stats_admin.html", duck=duck, duck_pictures=duck_pictures)
    
@admin_blueprint.route("/duck_stats/admin/<duck_id>", methods=["POST"])
def admin_page_edit_duck_post(duck_id):
    duck = select_duck_by_id(duck_id)
    duck.name = request.form["name"]
    duck.health = int(request.form["health"])
    duck.attack = int(request.form["attack"])
    duck.defense = int(request.form["defense"])
    duck.speed = int(request.form["speed"])
    duck.image = request.form["duck_image"]
    update_duck(duck)
    return redirect("/admin")

@admin_blueprint.route("/admin/delete/duck/<duck_id>", methods=["POST"])
def admin_page_delete_duck(duck_id):
    remove_duck(select_duck_by_id(duck_id))
    return redirect("/admin")


@admin_blueprint.route("/gym_class_edit/admin/<gc_id>", methods = ["GET"])
def edit_gym_class_get(gc_id):
    gym_class = select_class_by_id(gc_id)
    return render_template("admin/edit_gym_class_admin.html", gym_class = gym_class)

@admin_blueprint.route("/gym_class_edit/admin/<gc_id>", methods = ["POST"])
def edit_gym_class_post(gc_id):
    gym_class = Gym_class(**request.form, id=gc_id)
    update_gym_class(gym_class)
    return redirect("/admin")

@admin_blueprint.route("/admin/delete/<gc_id>", methods =["POST"])
def delete_gym_class(gc_id):
    gym_class = select_class_by_id(gc_id)
    remove_class(gym_class)
    return redirect("/admin")

