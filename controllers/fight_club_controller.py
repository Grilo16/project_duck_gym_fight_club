from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import select_duck_by_id


from repositories.battle_repository import delete_battle_by_object, get_all_finished_battles, get_all_ongoing_battles, select_battle_by_id, select_battles_ongoing_by_duck
from repositories.battle_repository import register_battle
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
    all_battles_finished = get_all_finished_battles()
    all_battles_ongoing = get_all_ongoing_battles()
    return render_template("fight_club/fight_log.html", all_battles_finished=all_battles_finished, all_battles_ongoing=all_battles_ongoing)

@fight_club_blueprint.route("/fight_club/battles", methods = ["POST"])
def show_battles_from_duck_redirect():
    duck = select_duck_by_id(request.form["duck"])
    return redirect(f"/fight_club/duck/{duck.id}/battles")

@fight_club_blueprint.route("/fight_club/duck/<duck_id>/battles")
def show_battles_from_duck(duck_id):
    duck = select_duck_by_id(duck_id)
    battles_won = select_battles_won_by_duck(duck)
    battles_lost = select_battles_lost_by_duck(duck)
    battles_ongoing = select_battles_ongoing_by_duck(duck)
    return render_template("fight_club/show_battles_from_duck.html", duck=duck, battles_won=battles_won, battles_lost=battles_lost, battles_ongoing=battles_ongoing)

@fight_club_blueprint.route("/fight_club/battle/<int:battle_id>/delete", methods=["POST"])
def delete_battle(battle_id):
    battle = select_battle_by_id(battle_id)
    print(battle.id, "lalalal")
    delete_battle_by_object(battle)
    return redirect("/fight_club/fight_log")