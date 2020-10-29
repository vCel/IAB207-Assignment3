
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


# creates the login information
class LoginForm(FlaskForm):
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):

    firstName = StringField("First Name", validators=[InputRequired()])
    lastName = StringField("Last name", validators=[InputRequired()])
    user_name = StringField("username", validators=[InputRequired()])
    email = StringField("Email Address", validators=[
        Email("Please enter a valid email")])

    # add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")
