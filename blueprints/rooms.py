from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
import re

rooms = Blueprint('rooms', __name__, url_prefix='/rooms', static_folder="static", template_folder="/rooms/")
