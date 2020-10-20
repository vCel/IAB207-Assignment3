from flask import Blueprint, render_template
from .models import Auction

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login')
def login():
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
