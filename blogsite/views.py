from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@views.route('/<variable>')
def variable_page(variable):
    return render_template("home.html")