from db.run_sql import run_sql
from models.duck import Duck

def add_duck_to_class(duck, gym_class):
    sql = "INSERT INTO ducks_in_classes (duck_id, gym_class_id) VALUES (%s, %s)"
    values = [duck.id, gym_class.id]
    run_sql(sql, values)
    
def remove_duck_from_class(duck, gym_class):
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
    
