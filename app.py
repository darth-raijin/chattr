import os
from flask import Flask, session, request, redirect, render_template, url_for, flash
from flask_session import Session
from dotenv import load_dotenv
from datetime import date
import sys
import uuid
import random
import json
import css_builder


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
Session(app)


builder = css_builder.load_colors()

@app.route('/')
def index():
        return render_template("index.html")

if __name__ == '__main__':
    app.run(threaded=True)