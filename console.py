from models.duck import Duck
from repositories.duck_repository import new_duck
from repositories.duck_repository import select_duck_by_id
from repositories.duck_repository import update_duck
from repositories.duck_repository import get_all_ducks
from repositories.duck_repository import remove_duck

duck = Duck("Ducky to be selected", 420, 69, 9001)

remove_duck(select_duck_by_id(5))
list(map(lambda item : print(item.__dict__) ,get_all_ducks()))