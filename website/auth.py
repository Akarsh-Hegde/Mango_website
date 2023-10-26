from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user, current_user, login_user
from . import db
from .models import User

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and email == "admin@gmail.com":
            if check_password_hash(user.password,password):
                # flash("Logged in successfully, Admin - you have a bright future!", category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        elif user:
            if check_password_hash(user.password,password):
                # flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash("email does not exist", category="error")

    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist!', category='error')
        elif len(email) < 4:
            flash("email must be more than 4 char!",category= "error")
        elif len(first_name) < 1:
            flash("first name must be more than 1 char!", category="error")
        elif password1 != password2:
            flash("password dont match", category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))            
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            # login_user(user, remember = True)
            return redirect(url_for('auth.login'))
    return render_template("signup.html", user=current_user)