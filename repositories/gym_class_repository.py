from db.run_sql import run_sql
from models.gym_class import Gym_class

def new_gym_class_for_duckies(gym_class):
    sql = "INSERT INTO gym_classes (name, duration) VALUES (%s, %s) RETURNING id"
    values = [gym_class.name, gym_class.duration]
    gym_class.id = run_sql(sql, values)[0][0]
    return gym_class
    
def select_class_by_id(id):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    return Gym_class(**run_sql(sql, values)[0])

def update_gym_class(gym_class):
    sql = "UPDATE gym_classes SET name=%s, duration=%s where id = %s"
    values = [gym_class.name, gym_class.duration, gym_class.id]
    run_sql(sql, values)

def get_all_classes():
    sql = "SELECT * FROM gym_classes"
    return list(map(lambda class_info: Gym_class(**class_info), run_sql(sql)))

def remove_class(gym_class):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [gym_class.id]
    run_sql(sql, values)
