from auction import db
from auction.models import *
from auction import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("¡ DONE !")
