from flask import Blueprint, render_template, request, session
from auction.models import *
from auction.forms import *
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/listings')
def listings():
    return render_template('listings.html')


@main.route('/account')
def account():
    if "user" in session:
        user = session["user"]
        return render_template('account.html', user=user)
    return render_template('login.html')




@main.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template('login.html')


@main.route('/forgot')
def forgot():
    return render_template('forgotpass.html')


@main.route('/vehicle')
def vehicle():
    get_auction = new_auction()
    return render_template('vehicle.html',
                           title=get_auction.title,
                           description=get_auction.description,
                           details=get_auction.details,
                           startBid=get_auction.startBid,
                           bid=get_auction.bid)

'''
def new_auction():
    newAuction = Auction("2018 Honda Civic VTI-LX",
                         "description", "$15,000", "$20,000")
    newAuction.add_detail("brand", "Honda")
    newAuction.add_detail("model", "Civic")
    newAuction.add_detail("transmission", "Automatic")
    newAuction.add_detail("colour", "Dark Grey")
    newAuction.add_detail("body", "Sedan")
    newAuction.add_detail("year", 2018)
    newAuction.add_detail("mileage", "15,000km")
    newAuction.add_detail("rego", "000XYZ")

    return newAuction


def featured():
    newList = list()
    for i in range(4):
        newAuction = Auction("2015 Mercedes A180",
                             "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList


def recent():
    newList = list()
    for i in range(4):
        newAuction = Auction("2015 Mercedes A180",
                             "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList


def popular():
    newList = list()
    for i in range(5):
        newAuction = Auction("2015 Mercedes A180",
                             "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList
'''
