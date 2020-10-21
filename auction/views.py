from flask import Blueprint, render_template, request, session
from .models import Auction

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    get_featured = featured()
    get_recent = recent()
    get_popular = popular()
    return render_template('index.html',
                           featuredList=get_featured,
                           recentList=get_recent,
                           popularList=get_popular)


@bp.route('/listings')
def listings():
    return render_template('listings.html')


@bp.route('/sell')
def sell():
    return render_template('sell.html')


@bp.route('/account')
def account():
    if "user" in session:
        user = session["user"]
        return render_template('account.html', user=user)
    return render_template('login.html')


@bp.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["email"] #change to name later
        session["user"] = user
        return redirect(url_for("user"))
    return render_template('login.html')


@bp.route('/vehicle')
def vehicle():
    get_auction = new_auction()
    return render_template('vehicle.html',
                           title=get_auction.title,
                           description=get_auction.description,
                           details=get_auction.details,
                           startBid=get_auction.startBid,
                           bid=get_auction.bid)


def new_auction():
    newAuction = Auction("2018 Honda Civic VTI-LX", "description", "$15,000", "$20,000")
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
        newAuction = Auction("2015 Mercedes A180", "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList


def recent():
    newList = list()
    for i in range(4):
        newAuction = Auction("2015 Mercedes A180", "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList


def popular():
    newList = list()
    for i in range(5):
        newAuction = Auction("2015 Mercedes A180", "description", "$25,000", "$35,000", 60)
        newList.append(newAuction)

    return newList
