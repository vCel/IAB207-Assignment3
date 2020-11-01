from flask import Blueprint, render_template, request, session, redirect, url_for, request, flash
from auction.models import *
from auction.forms import *
from auction import db
from flask_login import current_user, login_required
from auction.sell.utils import save_picture
from datetime import datetime, timedelta

listings = Blueprint('listings', __name__)

@listings.route('/all_listings',methods=['POST','GET'])
def show():
    vehicles = Auction.query.all()
    if request.method == 'POST':
        bidamount = request.form['bidAmount']
        id = request.form['id']
        
        return redirect(url_for('listings.bid',id=id,bidamount=bidamount))
    return render_template('listings.html',vehicles=vehicles)

@listings.route('/bid/<int:id>/<bidamount>',methods=['POST','GET'])
@login_required
def bid(id,bidamount):

    car_to_bid = Auction.query.get(id)
    if car_to_bid.status != 'open':
        flash('This auction is closed','warning')
        return redirect(url_for('listings.vehicle',id=id))
    if float(bidamount) < car_to_bid.bid:
        flash('Amount must be higher','warning')
        return redirect(url_for('listings.vehicle',id=id))

    bid_obj = Bid(bid=float(bidamount),username=current_user.username,auction=car_to_bid)
    db.session.add(bid_obj)
    car_to_bid.bid = float(bidamount)
    car_to_bid.bidsMade += 1
    db.session.commit()
    flash('Bid success !','success')
    return redirect(url_for('listings.show'))

@listings.route('/car/<int:id>',methods=['POST','GET'])
def vehicle(id):
    vehicle = Auction.query.get(id)

    if request.method == 'POST':
        if vehicle.status != 'open':
            flash('This auction is closed','warning')
            return redirect(url_for('listings.vehicle',id=id))
        if float(request.form['newBidAmount']) < vehicle.bid:
            flash('Amount must be higher','warning')
            return redirect(url_for('listings.vehicle',id=id))

        bidamount = request.form['newBidAmount']
        bid_obj = Bid(bid=float(bidamount),username=current_user.username,auction=vehicle)
        db.session.add(bid_obj)
        vehicle.bid = bidamount
        vehicle.bidsMade += 1
        db.session.commit()
    timedelta = str(vehicle.auction_end - datetime.now()).split(":")
    days = timedelta[0]
    hours = timedelta[1]

    return render_template('vehicle.html',vehicle=vehicle,days=days,hours=hours)

@listings.route('/add_watchlist/<int:id>',methods=['POST','GET'])
@login_required
def add_watchlist(id):
    if Auction.query.get(id).status != 'open':
        flash('Cannot add to watchlist since status is closed','danger')
        return redirect(url_for('listings.vehicle',id=id))
    holder = current_user.watchlist
    if holder == None:
        holder = '{},'.format(id)
    else:
        if id in current_user.watchlist.split(','):
            flash('Item already in wl','danger')
            return redirect(url_for('listings.vehicle',id=id))
        holder += '{},'.format(id)
    current_user.watchlist = holder
    db.session.commit()
    flash('Added to watchlist','success')
    return redirect(url_for('listings.vehicle',id=id))
