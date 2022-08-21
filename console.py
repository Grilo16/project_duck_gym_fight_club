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
from repositories.ducks_in_classes_repository import is_duck_in_class


from repositories.battle_repository import add_battle_result
from repositories.battle_repository import select_battle_by_id
from repositories.battle_repository import select_battles_won_by_duck
from repositories.battle_repository import select_battles_lost_by_duck
from repositories.battle_repository import get_all_battles


# Seeding starts 
def seeding_db():
    # Add ducks
    duck1 = new_duck(Duck("Ducky", 42, 69, 3, 690))
    duck2 = new_duck(Duck("Psyduck", 69, 96, 1, 420))
    duck3 = new_duck(Duck("Donald", 105, 69, 4, 210))
    duck4 = new_duck(Duck("Shanda Duckyleer", 210, 69, 2,  1000))
    duck5 = new_duck(Duck("Eric The Master Duck", 420, 690, 10, 1000))
    duck6 = new_duck(Duck("test duck", 0, 0, 0, 100))
    

    # Add gym classes
    class1 = new_gym_class_for_duckies(Gym_class("Pond Swimming", "attack", 10))
    # Add 3 ducks to gym class 1
    add_duck_to_class(duck1, class1)
    add_duck_to_class(duck2, class1)
    add_duck_to_class(duck3, class1)

    class2 = new_gym_class_for_duckies(Gym_class("Flying high", "speed", 2))
    # Add 5 ducks to gym class 1
    add_duck_to_class(duck1, class2)
    add_duck_to_class(duck2, class2)
    add_duck_to_class(duck3, class2)
    add_duck_to_class(duck4, class2)
    add_duck_to_class(duck5, class2)

    class3 = new_gym_class_for_duckies(Gym_class("Ducking Around", "health", 9))
    # Add 2 ducks to gym class 3
    add_duck_to_class(duck3, class3)
    add_duck_to_class(duck4, class3)

    class4 = new_gym_class_for_duckies(Gym_class("Squishing", "defense", 9))
    # Add 2 ducks to gym class 4
    add_duck_to_class(duck2, class4)
    add_duck_to_class(duck3, class4)

    # Adding ducky battles 
    battle1 = add_battle_result(Battle(duck1, duck2, winner=duck2))
    battle2 = add_battle_result(Battle(duck1, duck3, winner=duck3))
    battle3 = add_battle_result(Battle(duck1, duck4, winner=duck1))
    battle4 = add_battle_result(Battle(duck1, duck5, winner=duck5))

    battle5 = add_battle_result(Battle(duck5, duck1, winner=duck5))
    battle6 = add_battle_result(Battle(duck5, duck2, winner=duck5))
    battle7 = add_battle_result(Battle(duck5, duck3, winner=duck5))
    battle8 = add_battle_result(Battle(duck5, duck4, winner=duck5))

    # SEEDING ENDS

# seeding_db()

ducky = select_duck_by_id(1)
test_duck = select_duck_by_id(6)
gym_class1 = select_class_by_id(1)
gym_class2 = select_class_by_id(2)
gym_class3 = select_class_by_id(3)
gym_class4 = select_class_by_id(4)

ducky.health = -10


test_battle = Battle(ducky, test_duck)
test_battle.fight_turn("gust", "peck")
print(test_battle)



# list(map(lambda item : print(item.__dict__) ,get_all_ducks()))
# list(map(lambda item : print(item.__dict__) ,get_all_classes()))
# list(map(lambda item : print(item.__dict__) ,get_all_battles()))