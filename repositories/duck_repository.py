from models.duck import Duck
from db.run_sql import run_sql

def new_duck(duck):
    sql = "INSERT INTO ducks (name, attack, defense, health) VALUES (%s, %s, %s, %s) RETURNING id" 
    values = [duck.name, duck.attack, duck.defense, duck.health]
    duck.id = run_sql(sql, values)[0][0]
    return duck
        
def select_duck_by_id(id):
    sql = "SELECT * FROM ducks WHERE id = %s"
    values = [id]
    return Duck(**run_sql(sql, values)[0])

def update_duck(duck):
    sql = "UPDATE ducks SET name = %s, attack = %s, defense = %s, health = %s WHERE id = %s" 
    values = [duck.name, duck.attack, duck.defense, duck.health, duck.id]
    run_sql(sql, values)
    
def get_all_ducks():
    sql = "SELECT * FROM ducks"
    return list(map(lambda duck_info: Duck(**duck_info), run_sql(sql)))
    
def remove_duck(duck):
    sql = "DELETE FROM ducks WHERE id = %s"
    values = [duck.id]
    run_sql(sql, values)
    