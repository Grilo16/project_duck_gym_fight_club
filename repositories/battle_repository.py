from db.run_sql import run_sql
from models.battle import Battle
from repositories.duck_repository import select_duck_by_id

def add_battle_result(battle):
    sql = "INSERT INTO battle_results (duck_1_id, duck_2_id, winner) VALUES (%s, %s, %s)"
    values = [battle.duck_1.id, battle.duck_2.id, battle.winner.id]
    run_sql(sql, values)
  
def select_battle_by_id(id):    
    sql = "SELECT * FROM battle_results WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    return Battle(select_duck_by_id(result["duck_1_id"]), select_duck_by_id(result["duck_2_id"]), result["id"], select_duck_by_id(result["winner"]))

def get_all_battles():
    sql ="SELECT * FROM battle_results"
    return list(map(lambda battle_info: Battle(select_duck_by_id(battle_info["duck_1_id"]), select_duck_by_id(battle_info["duck_2_id"]), battle_info["id"], select_duck_by_id(battle_info["winner"]) ), run_sql(sql)))

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
    
    