from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment, Category

views = Blueprint('views', __name__)



@views.route('/')
def home():
    posts = Post.query.all()
    category = Category.query.all()
    return render_template("home.html", user=current_user, posts=posts, category=category)

@views.route('/<variable>')
def variable_page(variable):
    category = Category.query.all()
    return render_template("home.html", category=category)