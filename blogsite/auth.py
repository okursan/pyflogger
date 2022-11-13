from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(location=url_for('views.home'))

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        new_user = User(username=username, password=generate_password_hash(
                password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('User created!')
        return redirect(url_for('views.home'))

    return render_template("register.html")
