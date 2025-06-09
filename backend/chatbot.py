import re
import uuid
from datetime import datetime
from models import db, Product, ChatSession, ChatMessage

class EcommerceChatbot:
    """Main chatbot class for handling e-commerce queries"""
    
    def __init__(self):
        self.greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon']
        self.search_keywords = ['find', 'search', 'looking for', 'show me', 'want']
        self.price_keywords = ['price', 'cost', 'expensive', 'cheap', 'budget']
        
    def process_query(self, message):
        """Process user message and return appropriate response"""
        message_lower = message.lower()
        
        # Handle greetings
        if any(greeting in message_lower for greeting in self.greetings):
            return self._greeting_response()
        
        # Handle product search
        if any(keyword in message_lower for keyword in self.search_keywords):
            return self._search_products(message)
        
        # Handle price queries
        if any(keyword in message_lower for keyword in self.price_keywords):
            return self._price_query(message)
        
        # Handle category browsing
        categories = ['laptop', 'phone', 'tablet', 'headphone', 'camera', 'speaker']
        for category in categories:
            if category in message_lower:
                return self._browse_category(category)
        
        # Default response
        return self._default_response()
    
    def _greeting_response(self):
        """Generate greeting response with available options"""
        products = Product.query.limit(3).all()
        
        response = {
            'message': "Hello! Welcome to our electronics store! 🛍️ How can I help you today?",
            'suggestions': [
                "Show me laptops",
                "Find phones under $500",
                "Browse headphones",
                "What's on sale?"
            ],
            'products': []
        }
        
        if products:
            response['products'] = [{
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'image_url': p.image_url,
                'category': p.category        } for p in products]
        
        return response
    
    def _search_products(self, message):
        """Search for products based on user query"""
        # Extract search terms
        search_terms = self._extract_search_terms(message)
        price_range = self._extract_price_range(message)
        
        # Build query
        query = Product.query
        
        if search_terms:
            for term in search_terms:
                query = query.filter(
                    Product.name.contains(term) | 
                    Product.description.contains(term) |
                    Product.category.contains(term)
                )
        
        if price_range:
            min_price, max_price = price_range
            if min_price:
                query = query.filter(Product.price >= min_price)
            if max_price:
                query = query.filter(Product.price <= max_price)
        
        products = query.limit(10).all()
        
        if products:
            # Create detailed product descriptions
            product_details = []
            for p in products:
                product_details.append(f"• **{p.name}** - ${p.price:.2f}\n  {p.description}\n  Stock: {p.stock} available")
            
            detailed_message = f"Great! I found {len(products)} products for you:\n\n" + "\n\n".join(product_details)
            
            response = {
                'message': detailed_message,
                'products': [{
                    'id': p.id,
                    'name': p.name,
                    'price': p.price,
                    'description': p.description,
                    'image_url': p.image_url,
                    'category': p.category,
                    'stock': p.stock
                } for p in products],
                'suggestions': [
                    "Tell me more about the first product",
                    "Show me cheaper options",
                    "Browse similar products",
                    "Add to cart"
                ]
            }
        else:
            # Suggest alternatives when no products found
            popular_products = Product.query.limit(3).all()
            response = {
                'message': "I couldn't find exactly what you're looking for, but here are some popular products you might like:",
                'products': [{
                    'id': p.id,
                    'name': p.name,
                    'price': p.price,
                    'description': p.description,
                    'image_url': p.image_url,
                    'category': p.category,
                    'stock': p.stock
                } for p in popular_products],
                'suggestions': [
                    "Show me laptops",
                    "Browse phones",
                    "View all categories",
                    "Help me find something specific"
                ]        }
        
        return response
    
    def _browse_category(self, category):
        """Browse products in a specific category"""
        products = Product.query.filter(
            Product.category.contains(category)
        ).limit(8).all()
        
        if products:
            # Create detailed category overview
            total_products = len(products)
            price_range = f"${min(p.price for p in products):.2f} - ${max(p.price for p in products):.2f}"
            
            category_intro = f"Here are our top {total_products} {category}s (Price range: {price_range}):\n\n"
            
            product_summaries = []
            for p in products:
                stock_status = "✅ In Stock" if p.stock > 0 else "❌ Out of Stock"
                product_summaries.append(f"• **{p.name}** - ${p.price:.2f} ({stock_status})\n  {p.description[:80]}...")
            
            detailed_message = category_intro + "\n\n".join(product_summaries)
            
            response = {
                'message': detailed_message,
                'products': [{
                    'id': p.id,
                    'name': p.name,
                    'price': p.price,
                    'description': p.description,
                    'image_url': p.image_url,
                    'category': p.category,
                    'stock': p.stock
                } for p in products],
                'suggestions': [
                    f"Show me more {category}s",
                    "Filter by price range",
                    "Compare these products",
                    "What's the best one?"
                ]
            }
        else:
            response = {
                'message': f"Sorry, we don't have {category}s in stock right now. But we have great alternatives!",
                'suggestions': [
                    "Browse other categories",
                    "Check back later",
                    "View similar products"
                ],
                'products': []
            }
        
        return response
    
    def _price_query(self, message):
        """Handle price-related queries"""
        price_range = self._extract_price_range(message)
        
        if price_range:
            min_price, max_price = price_range
            query = Product.query
            
            if min_price:
                query = query.filter(Product.price >= min_price)
            if max_price:
                query = query.filter(Product.price <= max_price)
            
            products = query.limit(8).all()
            
            if products:
                price_text = ""
                if min_price and max_price:
                    price_text = f"between ${min_price} and ${max_price}"
                elif min_price:
                    price_text = f"over ${min_price}"
                elif max_price:
                    price_text = f"under ${max_price}"
                
                response = {
                    'message': f"Here are products {price_text}:",
                    'products': [{
                        'id': p.id,
                        'name': p.name,
                        'price': p.price,
                        'description': p.description,
                        'image_url': p.image_url,
                        'category': p.category,
                        'stock': p.stock
                    } for p in products],
                    'suggestions': [
                        "Show me cheaper options",
                        "Find premium products",
                        "Compare prices"
                    ]
                }
            else:
                response = {
                    'message': f"Sorry, no products found in that price range.",
                    'suggestions': [
                        "Try different price range",
                        "Browse all products",
                        "Check for discounts"
                    ],
                    'products': []
                }
        else:
            # General price inquiry
            avg_price = db.session.query(db.func.avg(Product.price)).scalar()
            min_price = db.session.query(db.func.min(Product.price)).scalar()
            max_price = db.session.query(db.func.max(Product.price)).scalar()
            
            response = {
                'message': f"Our products range from ${min_price:.2f} to ${max_price:.2f}, with an average price of ${avg_price:.2f}",
                'suggestions': [
                    "Show me budget options",
                    "Find premium products",
                    "Browse by category"
                ],
                'products': []
            }
        
        return response
    
    def _default_response(self):
        """Default response when query is not understood"""
        return {
            'message': "I'm not sure I understand. Can you try rephrasing your question? Here are some things I can help you with:",
            'suggestions': [
                "Search for products",
                "Browse categories",
                "Check prices",
                "View recommendations"
            ],
            'products': []
        }
    
    def _extract_search_terms(self, message):
        """Extract search terms from user message"""
        # Remove common words and extract meaningful terms
        stop_words = {'i', 'want', 'to', 'find', 'show', 'me', 'a', 'an', 'the', 'for', 'looking'}
        words = re.findall(r'\b\w+\b', message.lower())
        return [word for word in words if word not in stop_words and len(word) > 2]
    
    def _extract_price_range(self, message):
        """Extract price range from user message"""
        # Look for price patterns like "$100", "under 500", "between 100 and 200"
        price_patterns = [
            r'under\s*\$?(\d+)',
            r'below\s*\$?(\d+)',
            r'less\s+than\s*\$?(\d+)',
            r'over\s*\$?(\d+)',
            r'above\s*\$?(\d+)',
            r'more\s+than\s*\$?(\d+)',
            r'between\s*\$?(\d+)\s*and\s*\$?(\d+)',
            r'\$(\d+)\s*to\s*\$?(\d+)',
            r'\$(\d+)'
        ]
        
        message_lower = message.lower()
        
        for pattern in price_patterns:
            match = re.search(pattern, message_lower)
            if match:
                groups = match.groups()
                if len(groups) == 1:
                    price = float(groups[0])
                    if 'under' in pattern or 'below' in pattern or 'less' in pattern:
                        return (None, price)
                    elif 'over' in pattern or 'above' in pattern or 'more' in pattern:
                        return (price, None)
                    else:
                        return (price - 50, price + 50)  # Range around the price
                elif len(groups) == 2:
                    return (float(groups[0]), float(groups[1]))
        
        return None

# Initialize chatbot instance
chatbot = EcommerceChatbot()

def process_message(user_id, message, session_id=None):
    """Process a chat message and return response"""
    try:
        # Create or get session
        if not session_id:
            session_id = str(uuid.uuid4())
        
        session = ChatSession.query.filter_by(session_id=session_id).first()
        if not session:
            session = ChatSession(session_id=session_id, user_id=user_id)
            db.session.add(session)
            db.session.commit()
        
        # Process message through chatbot
        response_data = chatbot.process_query(message)
        
        # Save message and response
        chat_message = ChatMessage(
            session_id=session.id,
            message=message,
            response=response_data['message']
        )
        db.session.add(chat_message)
        db.session.commit()
        
        # Add session_id to response
        response_data['session_id'] = session_id
        
        return response_data
        
    except Exception as e:
        db.session.rollback()
        return {
            'message': f"Sorry, I encountered an error: {str(e)}",
            'products': [],
            'suggestions': ["Try again", "Contact support"],
            'session_id': session_id
        }