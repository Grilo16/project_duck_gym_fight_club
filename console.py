
from models.duck import Duck
from models.gym_class import Gym_class
from models.fight import Fight

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

from repositories.ducks_in_classes_repository import add_duck_to_class
from repositories.ducks_in_classes_repository import get_ducks_in_class
from repositories.ducks_in_classes_repository import remove_duck_from_class


duck1 = Duck("Ducky", 420, 69, 1000, 14)
duck2 = Duck("Ducky from mary from accounts", 420, 69, 1000, 15)
duck3 = Duck("Shanda Duckyleer", 420, 69, 1000, 16)

d1vd2 = Fight(duck1, duck2)
while True:
    d1vd2.fight_turn("wing attack", "peck")
    print(d1vd2)
    if d1vd2.winner != 0:
        break



class1 = Gym_class("Pond Swimming", 90, 5)
class3 = Gym_class("Flying high", 90, 8)
class2 = Gym_class("Ducking Around", 90, 7)

# for i in range(10):
#     new_duck(duck)
#     new_gym_class_for_duckies(pond_swimming)

# for i in get_ducks_in_class(class2):
#     print(i.__dict__)

# print()




# list(map(lambda item : print(item.__dict__) ,get_all_ducks()))
# list(map(lambda item : print(item.__dict__) ,get_all_classes()))