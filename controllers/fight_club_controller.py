from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

fight_club_blueprint = Blueprint("fight_club", __name__)

@fight_club_blueprint.route("/fight_club")
def fight_club_home():
    return render_template("fight_club/fight_club_test.html")

@fight_club_blueprint.route("/fight_club", methods=["POST"])
def fight_club_home_post():
    if request.form["answer"] == "You do not quack about duck fight club":
        return redirect("/fight_club/enter")
    else:
        return redirect("/")
    
@fight_club_blueprint.route("/fight_club/enter")
def enter_fight_club():
    return render_template("fight_club/fight_club_homepage.html")