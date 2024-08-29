from flask import session, Blueprint, request, jsonify
from orders.models.order_model import Orders
from db.db import db
from datetime import datetime  # Asegúrate de importar datetime

order_controller = Blueprint('order_controller', __name__)

@order_controller.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Orders.query.all()
    result = [{
        'id': order.id,
        'userName': order.userName,
        'userEmail': order.userEmail,
        'saleTotal': order.saleTotal,
        'date': order.date
    } for order in orders]
    return jsonify(result)

@order_controller.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Orders.query.get_or_404(order_id)
    return jsonify({
        'id': order.id,
        'userName': order.userName,
        'userEmail': order.userEmail,
        'saleTotal': order.saleTotal,
        'date': order.date
    })

@order_controller.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        userName = data['user']['name']
        email = data['user']['email']

        # Calcular el total de la venta
        saleTotal = sum(product['quantity'] * get_product_price(product['id']) for product in data['products'])

        # Crear una nueva instancia de Orders
        new_order = Orders(
            userName=userName,
            userEmail=email,
            saleTotal=saleTotal,
            date=datetime.utcnow()  # Fecha actual
        )

        db.session.add(new_order)
        db.session.commit()

        return jsonify({'message': 'Orden creada exitosamente'}), 201

    except KeyError as e:
        print(f"KeyError: {e}")
        return jsonify({'error': f'Falta el campo: {str(e)}'}), 400
    except Exception as e:
        print(f"Error general: {e}")
        return jsonify({'error': str(e)}), 500

@order_controller.route('/api/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Orders.query.get_or_404(order_id)
    data = request.json
    order.userName = data['userName']
    order.userEmail = data['userEmail']
    order.saleTotal = data['saleTotal']
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'})

@order_controller.route('/api/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Orders.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})
