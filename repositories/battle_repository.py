from db.run_sql import run_sql

def add_battle_result(battle):
    sql = "INSERT INTO battle_results (duck_1_id, duck_2_id, winner) VALUES (%s, %s, %s)"
    values = [battle.duck1.id, battle.duck2.id, battle.winner]
    run_sql(sql, values)