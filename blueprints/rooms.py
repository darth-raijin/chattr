from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from models import user
import re
from services.database import Database
from models.user import User

rooms = Blueprint('rooms', __name__, url_prefix='/rooms',
                 static_folder="static", template_folder="/chatrooms/")
database = Database()

@rooms.route("/")
def root():
    return render_template("rooms/rooms.html")

@rooms.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        public = request.form['public']

        if database.create_room(name, description, public, current_user.get_id()):
            flash("Room created, go have fun!",
                  category="success")
            print(request.form)
            return request.form


        return redirect(url_for(create))
    elif request.method == "GET":
        return render_template("rooms/create.html")
