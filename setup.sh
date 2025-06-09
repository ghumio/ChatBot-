#!/bin/bash

# E-Commerce Chatbot Setup Script
echo "🛍️ Setting up E-Commerce Chatbot Application..."

# Create Python virtual environment
echo "📦 Creating Python virtual environment..."
cd backend
python -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Initialize database with sample data
echo "🗄️ Initializing database..."
python database.py

echo "✅ Backend setup complete!"

# Setup frontend
echo "🎨 Setting up frontend..."
cd ../frontend

# Install Node.js dependencies
echo "📥 Installing Node.js dependencies..."
npm install

echo "✅ Frontend setup complete!"

echo ""
echo "🎉 Setup complete! To run the application:"
echo ""
echo "Backend (Terminal 1):"
echo "  cd backend"
echo "  source venv/Scripts/activate  # (Windows)"
echo "  # source venv/bin/activate    # (Mac/Linux)"
echo "  python app.py"
echo ""
echo "Frontend (Terminal 2):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "📝 Demo credentials:"
echo "  Username: testuser"
echo "  Password: password123"
echo ""
echo "🌐 Application will be available at:"
echo "  Frontend: http://localhost:3000"
echo "  Backend API: http://localhost:5000"
