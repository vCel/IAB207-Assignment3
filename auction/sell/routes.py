from flask import Blueprint, render_template, request, session, redirect, url_for
from auction.models import *
from auction.forms import *
from auction import db
from flask_login import current_user, login_required
from auction.sell.utils import save_picture

post = Blueprint('post', __name__)

@post.route('/sell',methods=['GET','POST'])
@login_required
def sell():
    form = SellCar()
    if form.validate_on_submit():
        image = save_picture(form.image.data)
        auction_object = Auction(title=form.title.data,
                                 description=form.description.data,
                                 startBid=form.start_bid.data,
                                 bid=form.start_bid.data,
                                 status='open',
                                 brand=form.brand.data,
                                 model=form.model.data,
                                 transmision=form.transmission.data,
                                 colour=form.colour.data,
                                 body=form.body.data,
                                 year=form.year.data,
                                 rego=form.registration.data,
                                 mileage=form.mileage.data,
                                 location=form.location.data,
                                 auction_end=form.auction_end.data,
                                 image=image,
                                 user=current_user)
        db.session.add(auction_object)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('sell.html',form=form)
