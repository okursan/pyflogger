from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = "okursan"
        email = "omerdurmus@gmail.com"
        password = "123456"
        first_name = "Omer"
        last_name = "Durmus"
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect(location=url_for('views.home'))