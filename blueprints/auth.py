from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from models import user
import re
from services.database import Database
from forms.login import LoginForm
from models.user import User

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 static_folder="static", template_folder="/auth/")
database = Database()


@auth.route("/test")
def auth_test():
    result = database.get_user_by_id("admin")
    print(result)
    user = User(id=result["id"], email=result["email"],
                joined_rooms=result["joined_rooms"], friends=result["friends"])

    login_user(user)

    return current_user.get_all()


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        userDic = {
            "username": request.form.get('username'),
            "password": request.form.get('password'),
            "email": request.form.get('email')
        }
        # Validation of Email address and username
        if not re.match(r"[^@]+@[^@]+\.[^@]+.", userDic["email"]):
            return ('Invalid email address', 400)
        elif not re.match(r"^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$", userDic["username"]):
            return ('Invalid username', 400)

        if database.create_user(userDic["username"], userDic["email"], generate_password_hash(userDic["password"])):
            print("Creating user")
            login_user(User(id=userDic["username"], email=userDic["email"]))

            return redirect(url_for("index"))
        else:
            return ('Failed to create', 409)
    else:  # Handling GET
        return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        result = database.get_user_by_id(username)

        if result is None:
            flash("Username and/or password is incorrect, try again!",
                  category="error")
            return redirect(url_for(login))
        
        # Validation of password

        if check_password_hash(result["password"], password):
            user = User(id=result["id"], email=result["email"],
                        joined_rooms=result["joined_rooms"], friends=result["friends"])
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Username and/or password is incorrect, try again!",
                  category="error")
            return redirect(url_for(login))

        return redirect(url_for("index"))
    elif request.method == "GET":
        return render_template("auth/login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('recon.index'))


def loadHelper(self, user_id):
    return database.get_user_by_id(user_id)
