from flask import Blueprint, render_template
from . import db
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    abc = User.query.all()
    return render_template("home.html", abc=abc)

@views.route('/<variable>')
def variable_page(variable):
    return render_template("home.html")