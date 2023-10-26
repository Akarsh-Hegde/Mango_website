from flask import Blueprint, render_template
from flask_login import login_required,current_user

views = Blueprint('views',__name__)

@views.route('/')
# @login_required
def home():
    return render_template("index.html",user = current_user,page = "")

@views.route('/about')
def about():
    return render_template("about.html",user = current_user,page = "about")

@views.route('/product')
# @login_required
def product():
    return render_template("product.html",user = current_user,page = "product")

@views.route('/gallery')
def gallery():
    return render_template("gallery.html",user = current_user,page = "gallery")

@views.route('/contact')
def contact():
    return render_template("contact.html",user = current_user,page = "contact")