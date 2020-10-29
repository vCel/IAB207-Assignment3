from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
#from .models import User
from auction.forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user, UserMixin
from auction import db


# create a blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def authenticate():  # view function
    print('In Login View function')
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        # takes the hash and password
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            # this gives the url from where the login page was accessed
            nextp = request.args.get('next')
            print(nextp)
            if next is None or not nextp.startswith('/'):
                return redirect(url_for('index'))
            return redirect(nextp)
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')


# @bp.route('/register', methods=['GET', 'POST'])
# def authenticate():  # view function
#     print('In Register View function')
#     registration_form = RegistrationForm()
#     error = None
#     if(registration_form.validate_on_submit() == True):
#         user_name = registration_form.user_name.data
#         password = registration_form.password.data
#         u1 = User.query.filter_by(name=user_name).first()
#         if u1 is None:
#             error = 'Incorrect user name'
#         # takes the hash and password
#         elif not check_password_hash(u1.password_hash, password):
#             error = 'Incorrect password'
#         if error is None:
#             login_user(u1)
#             # this gives the url from where the login page was accessed
#             nextp = request.args.get('next')
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=registration_form, heading='Login')