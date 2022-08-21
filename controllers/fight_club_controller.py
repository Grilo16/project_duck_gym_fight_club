from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import select_duck_by_id


from repositories.battle_repository import get_all_battles
from repositories.battle_repository import add_battle_result
from repositories.battle_repository import select_battles_won_by_duck
from repositories.battle_repository import select_battles_lost_by_duck



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
    all_ducks = get_all_ducks()
    return render_template("fight_club/fight_club_homepage.html", all_ducks=all_ducks)


@fight_club_blueprint.route("/fight_club/fight_log")
def view_fight_log():
    all_battles = get_all_battles()
    return render_template("fight_club/fight_log.html", all_battles=all_battles)

@fight_club_blueprint.route("/fight_club/battles", methods = ["POST"])
def show_battles_from_duck_redirect():
    duck = select_duck_by_id(request.form["duck"])
    return redirect(f"/fight_club/duck/{duck.id}/battles")

@fight_club_blueprint.route("/fight_club/duck/<duck_id>/battles")
def show_battles_from_duck(duck_id):
    duck = select_duck_by_id(duck_id)
    battles_won = select_battles_won_by_duck(duck)
    battles_lost = select_battles_lost_by_duck(duck)
    return render_template("fight_club/show_battles_from_duck.html", duck=duck, battles_won=battles_won, battles_lost=battles_lost)