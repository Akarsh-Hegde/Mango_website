from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # product = db.relationship('product', backref='owned_user', lazy=True)
    carts = db.relationship('Cart', backref='owned_user', lazy=True)    #lazy to grab all items in one shot
    
class Mango(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dispatch_week = db.Column(db.Integer(), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    # cart_id = db.Column(db.Integer(), db.ForeignKey('cart.id'))
    # carts = db.relationship('Cart', backref='mango', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    quantity =  db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024),nullable=False,unique =True)
    img = db.Column(db.Text, nullable=False, unique=True)
    img_name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    # cart_id = db.Column(db.Integer(), db.ForeignKey('cart.id'))
    # carts = db.relationship('Cart', backref='product', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    quantity =  db.Column(db.Integer(), nullable=False, default=1)
    description = db.Column(db.String(length=1024),nullable=False)

    owner = db.Column(db.Integer,db.ForeignKey('user.id'))
    # product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    # mango_id = db.Column(db.Integer(), db.ForeignKey('mango.id'))

    def __repr__(self):
        return f'Cart {self.name}'

# class Img(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     img = db.Column(db.Text, nullable=False)
#     name = db.Column(db.Text, nullable=False)
#     mimetype = db.Column(db.Text, nullable=False)