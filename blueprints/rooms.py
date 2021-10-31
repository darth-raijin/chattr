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
def room_root():

    return render_template("rooms/rooms.html")