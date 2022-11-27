from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment, Category

views = Blueprint('views', __name__)

@views.route('/')
def home():
    posts = Post.query.all()
    category = Category.query.all()
    return render_template("home.html", user=current_user, posts=posts, category=category)

@views.route('/cat/<cat_id>')
def variable_category(cat_id):
    category = Category.query.all()
    posts = Post.query.filter_by(category=cat_id)
    return render_template("home.html", category=category, posts=posts)

@views.route('/post/<post_id>', methods=['GET', 'POST'])
def variable_post(post_id):
    category = Category.query.all()
    post = Post.query.filter_by(id=post_id).first()
    comments = Comment.query.filter_by(post_id=post_id)
    
    if request.method == 'POST':
        comment = request.form.get("editor")
        author = request.form.get("author")
        new_comment = Comment(content=comment, author=author, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment created!')
        return redirect(url_for('views.variable_post', post_id=post_id))
    return render_template("post_single.html", category=category, post=post, comments=comments)