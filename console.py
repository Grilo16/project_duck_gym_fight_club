
from models.duck import Duck
from models.gym_class import Gym_class
from models.battle import Battle

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

from repositories.battle_repository import add_battle_result
from repositories.battle_repository import select_battle_by_id
from repositories.battle_repository import select_battles_won_by_duck
from repositories.battle_repository import select_battles_lost_by_duck
from repositories.battle_repository import select_all_battles


# duck1 = Duck("Ducky", 420, 69, 1000, 14)
# duck2 = Duck("Ducky from mary from accounts", 420, 69, 1000, 15)
# duck3 = Duck("Shanda Duckyleer", 420, 69, 1000, 16)

duck1 = select_duck_by_id(1)
duck2 = select_duck_by_id(2)
duck3 = select_duck_by_id(3)

# battle1 = Battle(duck3, duck2)
# while True:
#     battle1.fight_turn("gust", "wing attack")
#     if battle1.winner:
#         add_battle_result(battle1)
#         break

battles_won_by_duck = select_battles_won_by_duck(duck1)
battles_lost_by_duck = select_battles_lost_by_duck(duck1)

for battle in battles_won_by_duck:
    print(f"Competitor one was {battle.duck_1.name}")
    print(f"Competitor two was {battle.duck_2.name}")
    print(f"The winner was {battle.winner.name}")
    print()



# print(duck1.__dict__)
# print(duck2.__dict__)
# print(duck3.__dict__)

# d1vd2 = Battle(duck1, duck2)
# while True:
#     d1vd2.fight_turn("wing attack", "peck")
#     print(d1vd2)
#     if d1vd2.winner:
#         break



class1 = Gym_class("Pond Swimming", 90, 1)
class3 = Gym_class("Flying high", 90, 2)
class2 = Gym_class("Ducking Around", 90, 3)

# add_duck_to_class(duck1, class1)
# add_duck_to_class(duck2, class1)
# add_duck_to_class(duck3, class1)

# add_duck_to_class(duck1, class2)
# add_duck_to_class(duck2, class2)

# for i in range(10):
#     new_duck(duck)
#     new_gym_class_for_duckies(pond_swimming)

# for i in get_ducks_in_class(class2):
#     print(i.__dict__)

# print()




# list(map(lambda item : print(item.__dict__) ,get_all_ducks()))
# list(map(lambda item : print(item.__dict__) ,get_all_classes()))