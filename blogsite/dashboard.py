from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment

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
        new_post = Post(title=title, content=content, author=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created!')
        return redirect(url_for('dashboard.post_list'))
    return render_template("post_add.html")