from auction import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    watchlist = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pass_hash = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)
    posts = db.relationship('Auction', backref='user', lazy=True)



class Auction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    startBid = db.Column(db.Float, nullable=False)
    bid = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    transmision = db.Column(db.String(100), nullable=False)
    colour = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(100), nullable=False)
    rego = db.Column(db.String(100), nullable=False)
    mileage = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    auction_end = db.Column(db.DateTime, nullable=False)
    bidsMade = db.Column(db.Integer,nullable=True,default=0)
    image = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)