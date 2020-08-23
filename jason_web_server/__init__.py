from flask import Flask,render_template,url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)    

app.config["SECRET_KEY"] = "533c9456db724a12c03b32578b057a7e279260e1d529de71ca9d0a9c7c1350ed"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from jason_web_server import routes