from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required,current_user
from .models import Product, User, Cart, Mango
from . import db
from werkzeug.utils import secure_filename

admin = Blueprint('admin',__name__)

@admin.route('/admin_page', methods=['GET', 'POST'])
# @login_required
def admin_page():
    if request.method == "POST":
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        description = request.form.get('description')
        img = request.files['img']
        filename = secure_filename(img.filename)
        mimetype = img.mimetype

        id = request.form.get('id')   
        product_check = Product.query.filter_by(id=id).first()
        
        if request.form.get('add') == 'Add':
            if product_check:
                flash("Product already exists", category="error")
            else:  
                new_product = Product(name=name, price=price, quantity=quantity, description=description, img=img.read(), img_name=filename, mimetype=mimetype)
                db.session.add(new_product)
                db.session.commit()
                flash('Product Added!', category='success')
                return redirect(url_for("admin.admin_page"))
        
        id = request.form.get('id')   
        product = Product.query.filter_by(id=id).first()

        if request.form.get('remove') == 'Remove':
            db.session.delete(product)
            db.session.commit()
            flash('product Removed!', category='success')
            return redirect(url_for("products.admin_page"))

        if  request.form.get('edit') == 'Edit':
            # db.session.delete(item)
            # db.session.commit()
            if product:
                name = request.form.get('name')
                price = request.form.get('price')
                quantity = request.form.get('quantity')
                description = request.form.get('description')
                img = request.files['img']
                filename = secure_filename(img.filename)
                mimetype = img.mimetype
                product1 = Product(name=name, price=price, quantity=quantity, description=description, img=img.read(), img_name=filename, mimetype=mimetype)
                db.session.add(product1)
                db.session.commit()
                # flash('Product Updated(delete+add=edit)!', category='success')
                return redirect(url_for("admin.admin_page"))
            else:
                flash("Product doesnt exists", category="error")

    products = Product.query.all()
    carts = Cart.query.all()

    return render_template("admin.html", user=current_user, page = "contact", carts=carts, products=products)



