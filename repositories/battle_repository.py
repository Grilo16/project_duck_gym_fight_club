from db.run_sql import run_sql
from models.battle import Battle
from repositories.duck_repository import select_duck_by_id

def register_battle(battle):
    sql = "INSERT INTO battle_results (duck_1_id, duck_2_id, winner) VALUES (%s, %s, %s) RETURNING id"
    if battle.winner:
        values = [battle.duck_1.id, battle.duck_2.id, battle.winner.id]
    else:
        values = [battle.duck_1.id, battle.duck_2.id, battle.winner]
    battle.id= run_sql(sql, values)[0][0]
    return battle
        
def select_battle_by_id(id):
    sql = "SELECT * FROM battle_results WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]    
    duck1 = select_duck_by_id(result["duck_1_id"])
    duck2 = select_duck_by_id(result["duck_2_id"])
    if result["winner"] == None:
        return Battle(duck1, duck2, result["id"])
    winning_duck = select_duck_by_id(result["winner"])
    return Battle(duck1, duck2, result["id"], winning_duck)

def get_all_finished_battles():
    sql ="SELECT * FROM battle_results WHERE winner IS NOT NULL"
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"], select_duck_by_id(battle_info["winner"]) ), run_sql(sql)))

def get_all_ongoing_battles():
    sql ="SELECT * FROM battle_results WHERE winner is NULL"
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"]), run_sql(sql)))

def select_battles_won_by_duck(duck):
    sql ="""
        	select br.* from ducks
            join battle_results br 
            on winner = ducks.id 
            where winner = %s
            
         """
    values = [duck.id]   
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"], select_duck_by_id(battle_info["winner"]) ), run_sql(sql, values)))
    
def select_battles_lost_by_duck(duck):
    sql ="""
            select * from battle_results br 
            where %s in (duck_1_id, duck_2_id)
            and winner != %s;
            
         """
    values = [duck.id, duck.id]   
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"], select_duck_by_id(battle_info["winner"]) ), run_sql(sql, values)))
    
def select_battles_ongoing_by_duck(duck):
    sql ="""
            select * from battle_results br 
            where %s in (duck_1_id, duck_2_id)
            and winner is NULL;
            
         """
    values = [duck.id]   
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"]), run_sql(sql, values)))

def update_battle(battle):
    sql = "UPDATE battle_results SET duck_1_id=%s, duck_2_id=%s, winner=%s where id = %s"
    values = [battle.duck_1.id, battle.duck_2.id, battle.winner.id, battle.id]
    run_sql(sql, values)
    
def delete_battle_by_object(battle):
    sql = "DELETE FROM battle_results WHERE id = %s"
    values = [battle.id]
    run_sql(sql, values)
    