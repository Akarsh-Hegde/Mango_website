from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, send_file
from flask_login import login_required,current_user
from .models import Product, User, Cart, Mango
from . import db
from io import BytesIO


products = Blueprint('products',__name__)

@products.route('/buymango', methods=['GET','POST'])
# @login_required
def buymango():
    if request.method == 'POST':
        week = request.form.get('week')
        grade = request.form.get('flexRadioDefault')
        quantity = request.form.get('quantity')

        if grade=="A1+":
            price = 500
        elif grade=="A1":
            price = 400
        elif grade=="1":
            price = 350
        elif grade=="2":
            price = 300
        elif grade=="3":
            price = 250
        else:
            price = 200

        cart = Cart.query.filter_by(owner=current_user.id, name="Mango, Delivery: " + week + ", Size: " + grade).first()
        if cart:
            cart.quantity += int(quantity)
            db.session.commit()
            # flash('Product updates!', category='success')
            return redirect(url_for("products.buymango"))
        else:
            
            new_cart_product = Cart(name="Mango, Delivery: " + week + ", Size: " + grade, price=price, quantity=quantity, description="Alphanso Mango", owner=current_user.id)
            db.session.add(new_cart_product)
            db.session.commit()
            # flash('Product Added/Purchased!', category='success')
            return redirect(url_for("products.buymango"))

    return render_template("buymango.html",user = current_user,page = "buymango")

# @products.route('/process_option', methods=['POST'])
# def process_option():
#     selected_option = request.json['selected_option']
#     # Process the selected option as needed
#     result = f"Selected option: {selected_option}"
#     return jsonify(result=result)


@products.route('/buyproducts', methods=['GET','POST'])
# @login_required
def buyproducts():
    if request.method == "POST":

        id = request.form.get('product_id') 
        product = Product.query.filter_by(id=id).first()
        cart = Cart.query.filter_by(owner=current_user.id, name= product.name).first()
        if cart:
            cart.quantity += 1
            db.session.commit()
            # flash('Product updates!', category='success')
            return redirect(url_for("products.buyproducts"))
        else:
            new_cart_product = Cart(name=product.name, price=product.price, description=product.description, owner=current_user.id)
            db.session.add(new_cart_product)
            db.session.commit()
            # flash('Product Added/Purchased!', category='success')
            return redirect(url_for("products.buyproducts"))

    products = Product.query.all()
    return render_template("buyproducts.html", user = current_user, products=products)

@products.route('/download/<int:product_id>')
def download(id):
    product = Product.query.get_or_404(id)
    return send_file(
        BytesIO(product.img),
        mimetype=product.mimetype,
        download_name=product.img_name
    )

@products.route('/cart', methods=['GET','POST'])
# @login_required
def cart():
    if request.method == "POST":

        id = request.form.get('id')   
        cart_item = Cart.query.filter_by(id=id).first()
        product = Product.query.filter_by(id=id).first()
        mango = Mango.query.filter_by
        if request.form.get('remove') == 'Remove':
            db.session.delete(cart_item)
            db.session.commit()
            # flash('Item Removed!', category='success')
            return redirect(url_for("products.cart"))

        elif request.form.get('buy') == 'Buy Now':

            # Add Payment Gateway
            product.quantity -= cart_item.quantity
            db.session.delete(cart_item)
            db.session.commit()
            # flash('Item Bought!', category='success')
            return redirect(url_for("products.cart"))
        
    carts = Cart.query.filter(Cart.owner==current_user.id)
    return render_template("cart.html", user = current_user, page = "contact", carts = carts)