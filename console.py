from datetime import datetime
from models.duck import Duck
from models.gym_class import Gym_class
from repositories.duck_repository import new_duck
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import update_duck
from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import remove_duck
from repositories.gym_class_repository import new_gym_class_for_duckies
from repositories.gym_class_repository import select_class_by_id
from repositories.gym_class_repository import update_gym_class
from repositories.gym_class_repository import get_all_classes
from repositories.gym_class_repository import remove_class




duck = Duck("Ducky to be selected", 420, 69, 9001)

pond_swimming = Gym_class("Pond Swimming", 90)

new_gym_class_for_duckies(pond_swimming)

print(pond_swimming.__dict__)

ducky_flight = select_class_by_id(2)
ducky_flight.name = "ducky Flight"
update_gym_class(ducky_flight)
print(select_class_by_id(2).__dict__)

remove_class(select_class_by_id(2))

list(map(lambda item : print(item.__dict__) ,get_all_ducks()))
list(map(lambda item : print(item.__dict__) ,get_all_classes()))