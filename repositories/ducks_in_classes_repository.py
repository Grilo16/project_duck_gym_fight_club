from db.run_sql import run_sql
from models.duck import Duck
from models.gym_class import Gym_class
from repositories.duck_repository import update_duck

def add_duck_to_class(duck, gym_class):
    sql = "INSERT INTO ducks_in_classes (duck_id, gym_class_id) VALUES (%s, %s)"
    values = [duck.id, gym_class.id]
    run_sql(sql, values)
    
def remove_duck_from_class(duck, gym_class):
    if is_duck_in_class(duck, gym_class):
        duck.stat_up(gym_class)
        update_duck(duck)
    sql = "DELETE FROM ducks_in_classes WHERE duck_id = %s AND gym_class_id = %s"
    values = [duck.id, gym_class.id]
    run_sql(sql, values)
        
def get_ducks_in_class(gym_class):
    sql ="""SELECT ducks.* FROM ducks 
            JOIN ducks_in_classes as dic
            ON ducks.id = dic.duck_id
            WHERE dic.gym_class_id = %s"""
    values = [gym_class.id]
    return list(map(lambda duck_info: Duck(**duck_info), run_sql(sql, values)))

def get_classes_from_duck(duck):
    sql ="""select gc.* from ducks 
            join ducks_in_classes dic 
            on ducks.id  = dic.duck_id
            join gym_classes gc 
            on gc.id = dic.gym_class_id 
            where ducks.id = %s;"""
    values = [duck.id]
    return list(map(lambda gym_class_info: Gym_class(**gym_class_info), run_sql(sql, values)))
    
def is_duck_in_class(duck, gym_class):
    sql = """select * from ducks_in_classes dic 
             where duck_id = %s and gym_class_id = %s"""
    values = [duck.id, gym_class.id]
    results = run_sql(sql, values)
    if len(results) == 0:
        return False
    return True
    