import React, { useState, useEffect } from "react";
import axios from "axios";
import Login from "./components/Login";
import ChatBot from "./components/ChatBot";
import "./App.css";

// Configure axios defaults
axios.defaults.baseURL = "http://localhost:5000";

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username");

    if (token && username) {
      // Set axios default header for authenticated requests
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      setUser({ username, token });
    }

    setLoading(false);
  }, []);

  const handleLogin = (userData) => {
    // Store user data and token
    localStorage.setItem("token", userData.access_token);
    localStorage.setItem("username", userData.username);

    // Set axios default header
    axios.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${userData.access_token}`;

    setUser(userData);
  };

  const handleLogout = () => {
    // Clear stored data
    localStorage.removeItem("token");
    localStorage.removeItem("username");

    // Remove axios default header
    delete axios.defaults.headers.common["Authorization"];

    setUser(null);
  };

  if (loading) {
    return (
      <div className="app-loading">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <h1>🛍️ ElectroMart Chatbot</h1>
          {user && (
            <div className="user-info">
              <span>Welcome, {user.username}!</span>
              <button onClick={handleLogout} className="logout-btn">
                Logout
              </button>
            </div>
          )}
        </div>
      </header>

      <main className="app-main">
        {user ? <ChatBot user={user} /> : <Login onLogin={handleLogin} />}
      </main>
    </div>
  );
}

export default App;
