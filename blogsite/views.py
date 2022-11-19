from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment

views = Blueprint('views', __name__)

@views.route('/')
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@views.route('/<variable>')
def variable_page(variable):
    return render_template("home.html")