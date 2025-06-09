from models import db, User

def register_user(username, email, password):
    """Register a new user"""
    try:
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return False, "Username already exists"
        
        if User.query.filter_by(email=email).first():
            return False, "Email already registered"
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        return True, "User registered successfully"
        
    except Exception as e:
        db.session.rollback()
        return False, f"Registration failed: {str(e)}"

def authenticate_user(username, password):
    """Authenticate user login"""
    try:
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            return user
        
        return None
        
    except Exception as e:
        return None