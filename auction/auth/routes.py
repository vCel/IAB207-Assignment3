from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from auction.models import User
from auction.forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user, UserMixin, current_user
from auction import db


# create a blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():  # view function
    if current_user.is_authenticated:
        print('AUUUU')
    print('In Login View function')
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        email = form.email_id.data
        password = form.password.data
        user_exists = User.query.filter_by(email=email).first()
        if not user_exists:
            error = 'User does not exists'
            flash(error,'warning')
            return render_template('login.html', form=form, heading='Login')
        # takes the hash and password
        elif not user_exists.pass_hash == password:
            error = 'Incorrect password'
            flash(error,'warning')
            return render_template('login.html', form=form, heading='Login')
        else:
            login_user(user_exists)
            # this gives the url from where the login page was accessed

            return redirect(url_for('main.index'))


            flash(error,'warning')
    return render_template('login.html', form=form, heading='Login')


@auth.route('/register', methods=['GET', 'POST'])
def register():  # view function
    form = RegisterForm()
    if form.validate_on_submit():
        print('POST')
        first_name = form.firstName.data
        last_name = form.lastName.data
        user_name = form.user_name.data
        email = form.email.data
        password = form.password.data

        userExists = User.query.filter_by(email=email).first()
        userExists2 = User.query.filter_by(username=user_name).first()

        if not userExists and not userExists2:
            concatenated_name = first_name + ' ' + last_name
            user = User(name=concatenated_name,username=user_name,email=email,pass_hash=password)
            db.session.add(user)
            db.session.commit()
            print('User in db')

            flash('Created ! ','success')
        else:
            flash('User already exists !','warning')

    return render_template('register.html', form=form)
