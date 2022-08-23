from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request

from models.battle import Battle

from repositories.duck_repository import update_duck
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import get_all_ducks

from repositories.battle_repository import update_battle
from repositories.battle_repository import select_battle_by_id
from repositories.battle_repository import register_battle

battle_blueprint = Blueprint("battle", __name__)


# Select combatants page
@battle_blueprint.route("/fight_club/battle/select_combatants")
def select_combatants():
    all_ducks = get_all_ducks()
    return render_template("fight_club/battle/select_combatants.html", all_ducks=all_ducks)

# Select combatants page if duplicate duck
@battle_blueprint.route("/fight_club/battle/select_again")
def select_combatants_again():
    all_ducks = get_all_ducks()
    message = True
    return render_template("fight_club/battle/select_combatants.html", all_ducks=all_ducks, message=message)


# Display battle combatants post
@battle_blueprint.route("/fight_club/battle/verify", methods=["POST"])
def verify_and_register_battle():
    duck_1 = select_duck_by_id(request.form["duck_1"])
    duck_2 = select_duck_by_id(request.form["duck_2"])
    if duck_1.id == duck_2.id:
        return redirect("/fight_club/battle/select_again")
    battle = register_battle(Battle(duck_1, duck_2))
    return redirect(f"/fight_club/battle/{battle.id}")

# Pre-round page
@battle_blueprint.route("/fight_club/battle/<battle_id>")
def pre_round_page(battle_id):
    battle = select_battle_by_id(battle_id)
    print(battle)
    return render_template("fight_club/battle/battle_display.html", battle=battle)

# Decide who goes first
@battle_blueprint.route("/fight_club/battle/<battle_id>/decide_first_duck", methods=["POST"])
def start_battle_post(battle_id):
    battle = select_battle_by_id(battle_id)
    duck_order = battle.round_attack_order()
    first_duck = duck_order[0] 
    second_duck = duck_order[1]
    return redirect(f"/fight_club/battle/{battle.id}/attack/{first_duck.id}/{second_duck.id}")


# First duck attack choice
@battle_blueprint.route("/fight_club/battle/<battle_id>/attack/<first_duck_id>/<second_duck_id>")
def battle_round_first_attack(battle_id, first_duck_id, second_duck_id):
    battle = select_battle_by_id(battle_id)
    first_attacker = select_duck_by_id(first_duck_id)
    second_attacker = select_duck_by_id(second_duck_id)
    return render_template("fight_club/battle/round_first_attacker.html", first_attacker=first_attacker, second_attacker=second_attacker, battle=battle)

@battle_blueprint.route("/fight_club/battle/<battle_id>/register_first_attack", methods=["POST"])
def round_register_first_attack(battle_id):
    battle = select_battle_by_id(battle_id)
    next_attacker = battle.duck_attack(request.form["duck_id"], request.form["attack"])
    update_duck(battle.duck_1)
    update_duck(battle.duck_2)
    if not battle.has_winner():
        return redirect(f"/fight_club/battle/{battle.id}/battle_round/second_attacker/{next_attacker.id}")
    else:
        update_battle(battle)
        update_duck(battle.duck_1)
        update_duck(battle.duck_2)
        return redirect(f"/fight_club/battle/{battle.id}/results")
   
# Attacker 2 stuff here
@battle_blueprint.route("/fight_club/battle/<battle_id>/battle_round/second_attacker/<duck_id>")
def battle_round_second_attack(battle_id, duck_id):
    battle = select_battle_by_id(battle_id)
    attacker=select_duck_by_id(duck_id)
    return render_template("fight_club/battle/round_second_attacker.html", attacker=attacker, battle=battle)


@battle_blueprint.route("/fight_club/battle/<battle_id>/register_second_attack", methods=["POST"])
def round_register_second_attack(battle_id):
    battle = select_battle_by_id(battle_id)
    battle.duck_attack(request.form["duck_id"], request.form["attack"])
    
    update_duck(battle.duck_1)
    update_duck(battle.duck_2)
    if not battle.has_winner():
        return redirect(f"/fight_club/battle/{battle.id}/continue")
    else:
        update_battle(battle)
        return redirect(f"/fight_club/battle/{battle.id}/results")

@battle_blueprint.route("/fight_club/battle/<battle_id>/continue")
def continue_battle_post(battle_id):
    battle = select_battle_by_id(battle_id)
    duck_order = battle.round_attack_order()
    first_duck = duck_order[0] 
    second_duck = duck_order[1]
    return redirect(f"/fight_club/battle/{battle.id}/attack/{first_duck.id}/{second_duck.id}")    
    

@battle_blueprint.route("/fight_club/battle/<battle_id>/results")
def show_battle_results(battle_id):
    battle = select_battle_by_id(battle_id)
    return render_template("fight_club/battle/battle_result.html", battle = battle)
    

    
    
    
    
    