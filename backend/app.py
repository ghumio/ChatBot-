from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os
from models import db, User, Product, ChatSession, ChatMessage
from chatbot import process_message
from auth import authenticate_user, register_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

@app.route('/api/register', methods=['POST'])
def register():
    """User registration endpoint"""
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not all([username, email, password]):
            return jsonify({'error': 'All fields are required'}), 400
            
        success, message = register_user(username, email, password)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password required'}), 400
            
        user = authenticate_user(username, password)
        if user:
            access_token = create_access_token(identity=str(user.id))
            return jsonify({
                'access_token': access_token,
                'username': user.username
            }), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
@jwt_required()
def chat():
    """Process chat messages"""
    try:
        user_id = int(get_jwt_identity())  # Convert string back to int
        data = request.get_json()
        message = data.get('message')
        session_id = data.get('session_id')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Process the message through chatbot
        response = process_message(user_id, message, session_id)
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products"""
    try:
        products = Product.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'category': p.category,
            'price': p.price,
            'description': p.description,
            'stock': p.stock,
            'image_url': p.image_url
        } for p in products]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """Search products by query"""
    try:
        query = request.args.get('q', '')
        category = request.args.get('category', '')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        
        products_query = Product.query
        
        if query:
            products_query = products_query.filter(
                Product.name.contains(query) | 
                Product.description.contains(query)
            )
        
        if category:
            products_query = products_query.filter(Product.category == category)
            
        if min_price is not None:
            products_query = products_query.filter(Product.price >= min_price)
            
        if max_price is not None:
            products_query = products_query.filter(Product.price <= max_price)
        
        products = products_query.all()
        
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'category': p.category,
            'price': p.price,
            'description': p.description,
            'stock': p.stock,
            'image_url': p.image_url
        } for p in products]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat/history/<session_id>', methods=['GET'])
@jwt_required()
def get_chat_history(session_id):
    """Get chat history for a session"""
    try:
        user_id = get_jwt_identity()
        
        messages = ChatMessage.query.join(ChatSession).filter(
            ChatSession.user_id == user_id,
            ChatSession.session_id == session_id
        ).order_by(ChatMessage.timestamp).all()
        
        return jsonify([{
            'message': m.message,
            'response': m.response,
            'timestamp': m.timestamp.isoformat()
        } for m in messages]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)