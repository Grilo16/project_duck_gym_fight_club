from flask import Flask
from flask import render_template
from controllers.duck_controller import duck_blueprint
from controllers.gym_class_controller import gym_class_blueprint
from controllers.admin_controller import admin_blueprint

app = Flask(__name__)

app.register_blueprint(duck_blueprint)

app.register_blueprint(gym_class_blueprint)

app.register_blueprint(admin_blueprint)

@app.route("/")
def index():
    return render_template("index.html")