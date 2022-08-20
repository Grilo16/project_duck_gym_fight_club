from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from models.duck import Duck
from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import new_duck
from repositories.duck_repository import update_duck
from repositories.duck_repository import remove_duck

duck_blueprint = Blueprint("ducks", __name__)

# admin pages
@duck_blueprint.route("/admin")
def admin_page():
    all_ducks = get_all_ducks()
    return render_template("ducks/duck_admin_page.html", all_ducks=all_ducks)

@duck_blueprint.route("/duck_stats/admin/<duck_id>", methods=["GET"])
def admin_page_duck_stats(duck_id):
    duck = select_duck_by_id(duck_id)
    return render_template("ducks/view_duck_stats_admin.html", duck=duck)
    
@duck_blueprint.route("/duck_stats/admin/<duck_id>", methods=["POST"])
def admin_page_edit_duck(duck_id):
    duck = select_duck_by_id(duck_id)
    duck.name = request.form["name"]
    duck.health = int(request.form["health"])
    duck.attack = int(request.form["attack"])
    duck.defense = int(request.form["defense"])
    duck.speed = int(request.form["speed"])
    update_duck(duck)
    return redirect("/admin")

@duck_blueprint.route("/admin/delete/duck/<duck_id>", methods=["POST"])
def admin_page_delete_duck(duck_id):
    remove_duck(select_duck_by_id(duck_id))
    return redirect("/admin")

#  ===============================================================================


@duck_blueprint.route("/all_ducks")
def show_ducks():
    all_ducks = get_all_ducks()
    return render_template("ducks/show_ducks.html", all_ducks = all_ducks)

@duck_blueprint.route("/duck_stats/<duck_id>")
def show_duck_stats(duck_id):
    duck = select_duck_by_id(duck_id)
    return render_template("ducks/view_duck_stats.html", duck = duck)
    
@duck_blueprint.route("/create_duck", methods = ["GET"])
def create_duck_page():
    return render_template("ducks/create_duck.html")

@duck_blueprint.route("/create_duck", methods = ["POST"])
def save_new_duck():
    new_duck(Duck(request.form["duck_name"], 0, 0, 0, 100))
    return redirect("/all_ducks")

