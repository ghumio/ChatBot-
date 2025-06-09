# 🚀 E-Commerce Chatbot - Quick Setup Guide

## Prerequisites

- Python 3.8+ installed
- Node.js 14+ and npm installed
- Git (optional)

## 🐍 Backend Setup (Flask)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (bash)
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python app.py
```

Backend will be available at: `http://localhost:5000`

## ⚛️ Frontend Setup (React)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will be available at: `http://localhost:3000` (or the next available port)

## 🎯 Quick Start (Both Servers)

```bash
# Terminal 1: Start Backend
cd backend && python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt && python app.py

# Terminal 2: Start Frontend
cd frontend && npm install && npm start
```

## 📊 Project Structure (Cleaned)

```
├── README.md           # Project documentation
├── SETUP.md           # This setup guide
├── setup.sh           # Automated setup script
├── backend/           # Flask API server
│   ├── app.py         # Main Flask application
│   ├── auth.py        # Authentication logic
│   ├── chatbot.py     # Enhanced chatbot with detailed responses
│   ├── database.py    # Database initialization
│   ├── models.py      # SQLAlchemy models
│   ├── requirements.txt # Python dependencies
│   └── instance/      # Database files
│       └── ecommerce.db # SQLite database (53 products)
└── frontend/          # React client application
    ├── package.json   # Node.js dependencies
    ├── public/        # Static assets
    └── src/           # React components
        ├── App.js     # Main React app
        └── components/ # UI components
            ├── ChatBot.js    # Enhanced chatbot interface
            ├── Login.js      # Authentication
            └── ProductCard.js # Product display with SVG fallbacks
```

## ✅ What's Been Fixed

1. **Image Loading Issues**: All products now use embedded SVG images (no external dependencies)
2. **Chatbot Responses**: Enhanced with detailed product descriptions, pricing, and stock status
3. **Code Cleanup**: Removed unnecessary files and dependencies
4. **Project Size**: Reduced from ~500MB to 3.9MB (removed node_modules, venv, cache files)

## 🎮 Testing the Application

1. Register a new user account
2. Try chatbot commands:
   - "show me laptops"
   - "browse phones"
   - "help me find gaming accessories"
   - "what tablets do you have?"

The chatbot now provides detailed responses with product descriptions, pricing, and stock information!
