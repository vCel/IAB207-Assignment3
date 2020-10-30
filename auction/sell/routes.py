from flask import Blueprint, render_template, request, session
from auction.models import *
from auction.forms import *
from flask_login import current_user, login_required

post = Blueprint('post', __name__)

@post.route('/sell')
@login_required
def sell():
    form = SellCar()
    return render_template('sell.html',form=form)
