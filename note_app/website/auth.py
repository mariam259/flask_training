from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# import library that help in hashing the password
# These functions are useful for creating and verifying user passwords in web applications.
# They use secure hashing algorithms and random salts to prevent attackers from cracking the passwords easily
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # pass value from our flask app to our html file login.html
    # return render_template("login.html" , text="Testing" , boolean=False)

    # get data from the login Form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # search for the user on database
        user = User.query.filter_by(email=email).first()
        if user:  # if we find the user email then check if the enter password = the hash one in database
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                # call login_user function from flask_login to login user
                # keeps user login until he logout
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            else:
                flash("Incorrect password", category='error')
        else:  # if user doesn't exists in database
            flash("Email is not found", category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required  # we can't access logout page unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # save the value of the email from html file in a var called email
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # simple validation on our form

        user = User.query.filter_by(email=email).first()
        if user:  # check if it's new user or not
            flash("Email is already exists", category='error')
        elif len(email) < 4:
            flash("Email is too short", category='error')
        elif len(first_name) < 2:
            flash("Input valid name", category='error')
        elif password1 != password2:
            flash("password is not correct", category='error')
        elif len(password1) < 5:
            flash("Password is too short", category='error')
        else:
            # define a user
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            # save our password hashed with algorithm sha256

            # add new_user to database
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash("Account created", category='success')
            # after signUp go to home page (we use our blueprint name and the function we need to go(home))
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
