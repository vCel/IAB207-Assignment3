import secrets
import os
from flask import current_app
from PIL import  Image

def save_picture(form_picture):
    random_hex = secrets.token_hex(16)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path,
                                'static/img/products',
                                picture_fn)
    picture_fn = '/static/img/products/' + picture_fn

    size = (800, 1200)
    i = Image.open(form_picture)
    i.thumbnail(size)
    i.save(picture_path)
    return picture_fn
