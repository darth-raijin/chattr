from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from models.room import Room
import re
from services.database import Database
from models.user import User

rooms = Blueprint('rooms', __name__, url_prefix='/rooms',
                 static_folder="static", template_folder="/rooms/")
database = Database()


@login_required
@rooms.route("/")
def root():
    rooms = database.get_room_by_user(current_user.get_id())
    print(rooms)
    if rooms is not None:
        return render_template("rooms/rooms.html", rooms = rooms)
    return render_template("rooms/rooms.html")

@login_required
@rooms.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        public = request.form['public']

        if database.create_room(name, description, public, current_user.get_id()):
            flash("Room created, go have fun!",
                  category="success")
        return redirect(url_for(root))

    elif request.method == "GET":
        return render_template("rooms/create.html")


@login_required
@rooms.route("/connect", methods=["GET", "POST"])
def connect():
    room_id = request.args.get("id")
    # TODO get single Room that has ID
    result = database.get_room_by_id(room_id)

    if result:
        room = Room(result["_id"], result["name"] ,result["description"], result["members"], result["public"], result["admin"])
        print(room)
        current_user.set_current_room(room)

        if current_user.get_id() not in result["members"]:
            database.add_member_to_room(current_user.get_id(), result["_id"])

        return render_template("rooms/room.html", room = room)

    flash("That room does not exist!", "error")
    return redirect(url_for("rooms.root"))

@rooms.route("/invite", methods=["GET", "POST"])
def invite():
    room_id = request.args.get("id")
    print(room_id)
    # TODO get single Room that has ID
    result = database.get_room_by_id(room_id)

    if result:
        print("ROOM IS FOUND")
        if current_user.get_id() in result["admin"]:
            return render_template("rooms/invite.html", admin = True)
        flash("You're now a member!", "success")
        return redirect(url_for(rooms.root))

    flash("That room does not exist!", "error")
    return redirect(url_for("rooms.root"))

