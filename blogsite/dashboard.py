from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment, Category

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def board():
    return render_template("dashboard.html")

@dashboard.route('/posts')
@login_required
def post_list():
    posts = Post.query.all()
    return render_template("post_list.html", posts=posts)

@dashboard.route('/post_add', methods=['GET', 'POST'])
@login_required
def post_add():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("editor")
        category = request.form.get("category")
        new_post = Post(title=title, content=content, author=current_user.id, category=category)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created!')
        return redirect(url_for('dashboard.post_list'))
    category = Category.query.all()
    return render_template("post_add.html", category=category)

@dashboard.route('/categories', methods=['GET', 'POST'])
@login_required
def category_list():
    if request.method == 'POST':
        title = request.form.get("title")
        url = request.form.get("url")
        new_category = Category(title=title, url=url)
        db.session.add(new_category)
        db.session.commit()
        flash('Category created!')
        return redirect(url_for('dashboard.category_list'))
    category = Category.query.all()
    return render_template("category_list.html", category=category)