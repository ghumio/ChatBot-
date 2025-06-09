import React from "react";
import { ShoppingCart } from "lucide-react";

const ProductCard = ({ product, onProductClick }) => {
  const formatPrice = (price) => {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
    }).format(price);
  };

  const getStockStatus = (stock) => {
    if (stock === 0) return { text: "Out of Stock", className: "out-of-stock" };
    if (stock < 10) return { text: "Low Stock", className: "low-stock" };
    return { text: "In Stock", className: "in-stock" };
  };

  const stockStatus = getStockStatus(product.stock);

  return (
    <div
      className="product-card"
      onClick={() => onProductClick && onProductClick(product)}
    >
      {" "}
      <div className="product-image">
        <img
          src={
            product.image_url ||
            "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f3f4f6'/%3E%3Ctext x='150' y='100' text-anchor='middle' dy='0.3em' font-family='Arial, sans-serif' font-size='14' fill='%23374151'%3E" +
              product.name +
              "%3C/text%3E%3C/svg%3E"
          }
          alt={product.name}
          onError={(e) => {
            // Fallback to a simple SVG with product name
            e.target.src =
              "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23e5e7eb' stroke='%23d1d5db' stroke-width='2'/%3E%3Ctext x='150' y='85' text-anchor='middle' dy='0.3em' font-family='Arial, sans-serif' font-size='12' fill='%23374151'%3E" +
              encodeURIComponent(product.name) +
              "%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' dy='0.3em' font-family='Arial, sans-serif' font-size='16' fill='%23059669'%3E$" +
              product.price +
              "%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' dy='0.3em' font-family='Arial, sans-serif' font-size='10' fill='%236b7280'%3E" +
              encodeURIComponent(product.category) +
              "%3C/text%3E%3C/svg%3E";
          }}
        />
        <div className={`stock-badge ${stockStatus.className}`}>
          {stockStatus.text}
        </div>
      </div>
      <div className="product-info">
        <div className="product-category">
          {product.category?.charAt(0).toUpperCase() +
            product.category?.slice(1)}
        </div>

        <h3 className="product-name">{product.name}</h3>

        <p className="product-description">
          {product.description?.length > 100
            ? `${product.description.substring(0, 100)}...`
            : product.description}
        </p>

        <div className="product-footer">
          <div className="product-price">{formatPrice(product.price)}</div>

          {product.stock > 0 && (
            <button
              className="add-to-cart-btn"
              onClick={(e) => {
                e.stopPropagation();
                // Handle add to cart logic here
                console.log("Add to cart:", product.name);
              }}
            >
              <ShoppingCart size={16} />
              Add to Cart
            </button>
          )}
        </div>

        {product.stock > 0 && product.stock < 10 && (
          <div className="stock-warning">
            Only {product.stock} left in stock!
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductCard;
