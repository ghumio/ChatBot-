import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Send, LogOut, ShoppingBag, Bot, User as UserIcon } from "lucide-react";
import ProductCard from "./ProductCard";

const ChatBot = ({ user, onLogout }) => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);
  useEffect(() => {
    // Send initial greeting
    const sendInitialGreeting = async () => {
      setLoading(true);
      try {
        const response = await axios.post("/api/chat", {
          message: "hello",
          session_id: null,
        });

        const botResponse = {
          type: "bot",
          content: response.data.message,
          products: response.data.products || [],
          suggestions: response.data.suggestions || [],
          timestamp: new Date(),
        };

        setMessages([botResponse]);
        setSessionId(response.data.session_id);
      } catch (error) {
        const errorMessage = {
          type: "bot",
          content:
            "Welcome! I'm your shopping assistant. How can I help you today?",
          products: [],
          suggestions: ["Show me laptops", "Find phones", "Browse headphones"],
          timestamp: new Date(),
        };
        setMessages([errorMessage]);
      } finally {
        setLoading(false);
      }
    };

    sendInitialGreeting();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  const handleSendMessage = async (messageText = null) => {
    const message = messageText || inputMessage.trim();
    if (!message) return;

    // Add user message to chat
    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        content: message,
        timestamp: new Date(),
      },
    ]);
    setInputMessage("");

    setLoading(true);

    try {
      const response = await axios.post("/api/chat", {
        message: message,
        session_id: sessionId,
      });

      const botResponse = {
        type: "bot",
        content: response.data.message,
        products: response.data.products || [],
        suggestions: response.data.suggestions || [],
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, botResponse]);
      setSessionId(response.data.session_id);
    } catch (error) {
      const errorMessage = {
        type: "bot",
        content: "Sorry, I encountered an error. Please try again.",
        products: [],
        suggestions: [],
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    handleSendMessage(suggestion);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const formatTime = (timestamp) => {
    return timestamp.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <div className="header-left">
          <Bot className="bot-icon" />
          <div>
            <h2>Shopping Assistant</h2>
            <span className="status">Online</span>
          </div>
        </div>
        <div className="header-right">
          <span className="welcome-text">Welcome, {user.username}!</span>
          <button onClick={onLogout} className="logout-btn">
            <LogOut size={18} />
            Logout
          </button>
        </div>
      </div>

      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            <div className="message-header">
              {message.type === "bot" ? (
                <Bot className="message-icon bot-icon" />
              ) : (
                <UserIcon className="message-icon user-icon" />
              )}
              <span className="message-time">
                {formatTime(message.timestamp)}
              </span>
            </div>

            <div className="message-content">
              <p>{message.content}</p>

              {message.products && message.products.length > 0 && (
                <div className="products-grid">
                  {message.products.map((product) => (
                    <ProductCard
                      key={product.id}
                      product={product}
                      onProductClick={(product) => {
                        handleSendMessage(`Tell me more about ${product.name}`);
                      }}
                    />
                  ))}
                </div>
              )}

              {message.suggestions && message.suggestions.length > 0 && (
                <div className="suggestions">
                  <p className="suggestions-label">Try asking:</p>
                  <div className="suggestions-grid">
                    {message.suggestions.map((suggestion, idx) => (
                      <button
                        key={idx}
                        onClick={() => handleSuggestionClick(suggestion)}
                        className="suggestion-btn"
                      >
                        {suggestion}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="message bot">
            <div className="message-header">
              <Bot className="message-icon bot-icon" />
              <span className="message-time">Now</span>
            </div>
            <div className="message-content">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-container">
        <div className="chat-input">
          <textarea
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me about products, prices, or recommendations..."
            disabled={loading}
            rows={1}
          />
          <button
            onClick={() => handleSendMessage()}
            disabled={loading || !inputMessage.trim()}
            className="send-btn"
          >
            <Send size={18} />
          </button>
        </div>
        <div className="input-help">
          <ShoppingBag size={14} />
          <span>
            Try: "Show me laptops under $1000" or "Find wireless headphones"
          </span>
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
