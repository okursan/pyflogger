from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = "okursan"
        password = generate_password_hash("123456", method='sha256')
        new_user = User(username=username, password=password)
        login_user(user=new_user, remember=True)
        return redirect(url_for('views.home'))
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(location=url_for('views.home'))