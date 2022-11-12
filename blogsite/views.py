from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/<variable>')
def variable_page(variable):
    return render_template("home.html")