from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Post, Comment

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")