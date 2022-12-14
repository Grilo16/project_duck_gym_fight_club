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


from repositories.battle_repository import register_battle
from repositories.battle_repository import select_battle_by_id
from repositories.battle_repository import select_battles_won_by_duck
from repositories.battle_repository import select_battles_lost_by_duck


# Seeding starts 
def seeding_db():
    # Add ducks
    duck1 = new_duck(Duck("Ducky", 420, 69, 5, 6900, image="rdbp-gallery-14.png"))
    duck2 = new_duck(Duck("Psyduck", 69, 96, 1, 420, image="rdbp-gallery-12.png"))
    duck3 = new_duck(Duck("Donald", 105, 69, 4, 210, image="rdbp-gallery-11.png"))
    duck4 = new_duck(Duck("Shanda Duckyleer", 210, 69, 2,  4200, image="rdbp-gallery-16.png"))
    duck5 = new_duck(Duck("Eric The Master Duck", 420, 690, 5, 6900, image="rdbp-gallery-9.png"))
    duck6 = new_duck(Duck("Hoisin", 0, 0, 0, 100, image="rdbp-gallery-17.png"))
    

    # Add gym classes
    class1 = new_gym_class_for_duckies(Gym_class("Pond Swimming", "attack", 50))
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

    class3 = new_gym_class_for_duckies(Gym_class("Ducking Around", "health", 200))
    # Add 2 ducks to gym class 3
    add_duck_to_class(duck3, class3)
    add_duck_to_class(duck4, class3)

    class4 = new_gym_class_for_duckies(Gym_class("Squishing", "defense", 69))
    # Add 2 ducks to gym class 4
    add_duck_to_class(duck2, class4)
    add_duck_to_class(duck3, class4)

    # Adding ducky battles 
    battle1 = register_battle(Battle(duck1, duck2, winner=duck2))
    battle2 = register_battle(Battle(duck1, duck3, winner=duck3))
    battle3 = register_battle(Battle(duck1, duck4, winner=duck1))
    battle4 = register_battle(Battle(duck1, duck5, winner=duck5))

    battle5 = register_battle(Battle(duck5, duck1, winner=duck5))
    battle6 = register_battle(Battle(duck5, duck2, winner=duck5))
    battle7 = register_battle(Battle(duck5, duck3, winner=duck5))
    battle8 = register_battle(Battle(duck5, duck4, winner=duck5))

    # SEEDING ENDS

# seeding_db()

# View ducks
# create a duck
# show stats
# enrol in classes make him strong

# create a class
# enrol ducks, show the changes

# Edit ducks and classes

# go to fightclub

# Eric v ducky - demonstrate speed variability + defense
# Eric v Shanda - demonstrate speed superiority + stop halfway
# Psyduck v Donald - demonstrate victory 
# restart eric v shanda demonstrate restartability

# Show fight logs

#  Go to test page

# list(map(lambda item : print(item.__dict__) ,get_all_ducks()))
# list(map(lambda item : print(item.__dict__) ,get_all_classes()))
# list(map(lambda item : print(item.__dict__) ,get_all_battles()))

