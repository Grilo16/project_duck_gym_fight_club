from flask import Flask
from flask import render_template
from controllers.duck_controller import duck_blueprint
from controllers.gym_class_controller import gym_class_blueprint
from controllers.admin_controller import admin_blueprint
from controllers.ducks_in_classes_controller import ducks_in_classes_blueprint
from controllers.fight_club_controller import fight_club_blueprint
from repositories.duck_repository import get_all_ducks
from repositories.gym_class_repository import get_all_classes


app = Flask(__name__)

app.register_blueprint(duck_blueprint)

app.register_blueprint(gym_class_blueprint)

app.register_blueprint(admin_blueprint)

app.register_blueprint(ducks_in_classes_blueprint)

app.register_blueprint(fight_club_blueprint)

@app.route("/")
def index():
    all_ducks = get_all_ducks()
    all_classes = get_all_classes()
    return render_template("index.html", all_ducks = all_ducks, all_classes = all_classes)