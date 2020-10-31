
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
from wtforms.fields.html5 import DateField

# creates the login information
class LoginForm(FlaskForm):
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form

class RegisterForm(FlaskForm):

    firstName = StringField("First Name:", validators=[InputRequired()])
    lastName = StringField("Last name:", validators=[InputRequired()])
    user_name = StringField("username:", validators=[InputRequired()])
    email = StringField("Email Address:", validators=[
        Email("Please enter a valid email")])

    # add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password:", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password:")

    # submit button
    submit = SubmitField("Register")

class SellCar(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])
    brand = StringField("Brand", validators=[InputRequired()])
    model = StringField("Model", validators=[InputRequired()])
    transmission = SelectField("Transmission", choices=[('auto','Automatic'),('mech','Mechanic')],validators=[InputRequired()])
    colour = StringField("Colour", validators=[InputRequired()])
    body = StringField("Body Type", validators=[InputRequired()])
    year = StringField("Year", validators=[InputRequired()])
    registration = StringField("Registration", validators=[InputRequired()])
    mileage = StringField("Mileage", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    start_bid = FloatField("Starting bid", validators=[InputRequired()])
    auction_end = DateField("Auction End Date", validators=[InputRequired()])
    #image = FileField('Upload Image',validators=[DataRequired(),FileAllowed(['jpeg','png','jpg'])])
    image = FileField('Upload Image',validators=[DataRequired(),FileAllowed(['jpeg','png','jpg'])])
    submit = SubmitField("Create Listing")
