from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from auction.models import *
from auction.forms import *
from flask_login import current_user, login_required, logout_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    auctions = Auction.query.all()
    send = []
    for i in range(1,3):
        try:
            send.append(auctions[-i])
        except:
            break

    return render_template('index.html',recent=send)


@main.route('/account')
@login_required
def account():
    watchlist = []
    if current_user.watchlist != None:
        for element in current_user.watchlist.split(',')[:-1]:
            watchlist.append(Auction.query.get(int(element)))
    return render_template('account.html',watchlist=watchlist,auctions=current_user.posts)

@main.route('/close/<int:id>')
@login_required
def close_auction(id):
    if not Auction.query.get(id) in current_user.posts:
        abort(403)
    else:
        auction = Auction.query.get(id)
        auction.status = 'closed'
        db.session.commit()
        flash('Auction closed !','danger')
    return redirect(url_for('main.account'))

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


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
