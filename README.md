# 🛍️ E-Commerce Chatbot Application

A modern, full-stack e-commerce application with an AI-powered chatbot assistant built with Flask (backend) and React (frontend).

## 🚀 Current Status: FULLY FUNCTIONAL ✅

- ✅ Flask backend running on `http://localhost:5000`
- ✅ React frontend running on `http://localhost:3001`
- ✅ Database initialized with 53 sample products
- ✅ User authentication system working
- ✅ Image loading issues resolved (SVG embedded images)
- ✅ Enhanced chatbot with detailed product responses
- ✅ All API endpoints operational
- ✅ Responsive UI design complete
- ✅ Codebase cleaned and optimized

## ✨ Features

- **AI Chatbot Assistant**: Intelligent product recommendations and search
- **User Authentication**: Secure login and registration system
- **Product Catalog**: Comprehensive electronics inventory with working images
- **Real-time Chat**: Interactive conversation with the shopping assistant
- **Responsive Design**: Beautiful, mobile-friendly interface
- **Product Search**: Advanced filtering by category, price, and keywords
- **Error Handling**: Graceful image fallbacks and robust error management

## 🏗️ Tech Stack

### Backend

- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **Flask-JWT-Extended**: JWT authentication
- **Flask-CORS**: Cross-origin resource sharing
- **SQLite**: Database

### Frontend

- **React**: JavaScript library for building user interfaces
- **Axios**: HTTP client for API requests
- **Lucide React**: Beautiful icons
- **CSS3**: Modern styling with animations

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ installed
- Node.js 14+ installed
- Git (optional)

### Method 1: Automatic Setup (Recommended)

1. **Make the setup script executable:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

### Method 2: Manual Setup

#### Backend Setup

1. **Navigate to backend directory:**

   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database with sample data:**

   ```bash
   python database.py
   ```

5. **Start the Flask server:**
   ```bash
   python app.py
   ```

#### Frontend Setup

1. **Navigate to frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**

   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

## 🌐 Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## 🔐 Demo Credentials

```
Username: testuser
Password: password123
```

## 🎯 How to Use

1. **Login/Register**: Use the demo credentials or create a new account
2. **Start Chatting**: The chatbot will greet you automatically
3. **Search Products**: Try queries like:
   - "Show me laptops under $1000"
   - "Find wireless headphones"
   - "Browse gaming accessories"
   - "What's the cheapest phone?"
4. **Explore Products**: Click on products for more details
5. **Use Suggestions**: Click on suggested queries for quick searches

## 📁 Project Structure

```
📦 E-Commerce Chatbot
├── 📁 backend/
│   ├── app.py              # Main Flask application
│   ├── models.py           # Database models
│   ├── auth.py             # Authentication logic
│   ├── chatbot.py          # AI chatbot implementation
│   ├── database.py         # Database initialization
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── 📁 frontend/
│   ├── 📁 public/
│   │   └── index.html     # HTML template
│   ├── 📁 src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Styles
│   │   ├── index.js       # React entry point
│   │   └── 📁 components/
│   │       ├── Login.js   # Login/Register component
│   │       ├── ChatBot.js # Main chat interface
│   │       └── ProductCard.js # Product display component
│   └── package.json       # Node.js dependencies
├── setup.sh               # Automatic setup script
└── README.md              # This file
```

## 🛠️ Development

### Adding New Products

Edit `backend/database.py` and run:

```bash
python database.py
```

### Customizing the Chatbot

Modify the logic in `backend/chatbot.py` to add new conversation patterns or product recommendations.

### Frontend Styling

Update `frontend/src/App.css` to customize the appearance.

## 🎯 MANUAL TESTING GUIDE

### 1. Access the Application

- Open your browser and navigate to: `http://localhost:3002`
- You should see the beautiful E-Commerce Chatbot interface

### 2. Test User Registration

- Click "Don't have an account? Register here"
- Fill in the registration form with new credentials
- Verify successful registration message

### 3. Test User Login

- Use the test credentials:
  - Username: `testuser`
  - Password: `password123`
- Verify successful login and redirect to main app

### 4. Browse Products

- View the product catalog with images loading from Picsum
- Check different product categories (laptops, phones, tablets, etc.)
- Verify responsive design on different screen sizes

### 5. Test Chatbot

- Click on the chat interface
- Try messages like:
  - "I need a laptop for gaming"
  - "Show me headphones under $300"
  - "What cameras do you have?"
- Verify AI responses with product recommendations

### 6. Test Product Interactions

- Click on product cards to view details
- Try "Add to Cart" buttons (console logging implemented)
- Check stock status badges (In Stock, Low Stock, Out of Stock)

## 🔧 TROUBLESHOOTING

### React Server Issues

If the React server seems slow to start:

1. The app is accessible on `http://localhost:3002` even during compilation
2. Refresh the browser if you see loading screens
3. Check the terminal for "Compiled successfully" message

### Image Loading

- If images don't load, the fallback SVG placeholder will appear
- All products now use reliable Picsum photo service
- Error handling is built into the ProductCard component

### API Testing

Test backend endpoints directly:

```bash
# Get all products
curl http://localhost:5000/api/products

# Test registration
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"newuser","email":"new@example.com","password":"password123"}'

# Test login
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"password123"}'
```

## 🎉 SUCCESS METRICS

The application is considered **fully functional** when:

- ✅ Both servers are running (Flask on :5000, React on :3002)
- ✅ Products display with images in the browser
- ✅ User can register and login successfully
- ✅ Chatbot responds to user messages
- ✅ All UI components render properly
- ✅ No critical errors in browser console

**Current Status: ALL SUCCESS METRICS ACHIEVED! 🚀**

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

If you encounter any issues, please:

1. Check the troubleshooting section
2. Ensure all dependencies are installed
3. Verify both servers are running
4. Check browser console for errors

---

Made with ❤️ for modern e-commerce experiences
# ChatBot-
