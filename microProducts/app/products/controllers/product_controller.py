from flask import Blueprint, request, jsonify, session, g
from products.models.product_model import Products
from db.db import db
from datetime import timedelta


product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")

    #print(g.__dict__)

    products = Products.query.all()
    result = [{'id':product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity} for product in products]
    return jsonify(result)

# Get single product by id
@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print("obteniendo productos")
    product = Products.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity})

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    #new_user = Users(name="oscar", email="oscar@gmail", username="omondragon", password="123")
    new_product = Products(name=data['name'], price=data['price'], quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Update an existing user
@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    print("actualizando producto")
    product = Products.query.get_or_404(product_id)
    data = request.json
    product.name = data['name']
    product.price = data['price']
    product.quantity = data['quantity']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Delete an existing user
@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'product deleted successfully'})

#@user_controller.route('/api/login', methods=['POST'])
#def login():
#    data = request.json

#    username = data.get('username')
#    password = data.get('password')

#    if not username or not password:
#        return jsonify({'message': 'Missing username or password'}),400

#    user = Users.query.filter_by(username=username).first()

#    if not user:
#        return jsonify({'message': 'Invalid username or password'}), 401

#    #if not check_password_hash(user.password, password):
#    if user.password != password:
#        return jsonify({'message': 'Invalid username or password'}), 401

#    # Store user information in session
#    session['user_id'] = user.id
#    session['username'] = user.username
#    session['email'] = user.email  # Add other user information as needed

#    #g.user=user

#    #print(g.__dict__)
#    print("En session: ",session)

#    return jsonify({'message': 'Login successful'})
