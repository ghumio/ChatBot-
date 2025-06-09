from flask import Flask
from models import db, User, Product
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_sample_data():
    """Create sample products and test user"""
      # Sample electronics products
    products_data = [        # Laptops
        {"name": "MacBook Pro 16-inch", "category": "laptop", "price": 2499.99, "description": "Powerful laptop with M1 Pro chip, 16GB RAM, 512GB SSD", "stock": 15, "image_url": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f8f9fa'/%3E%3Ctext x='150' y='90' text-anchor='middle' font-family='Arial' font-size='14' fill='%23333'%3EMacBook Pro 16-inch%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' font-family='Arial' font-size='16' font-weight='bold' fill='%23059669'%3E$2499.99%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'%3ELaptop%3C/text%3E%3C/svg%3E"},
        {"name": "Dell XPS 13", "category": "laptop", "price": 1299.99, "description": "Ultra-thin laptop with Intel i7, 16GB RAM, 256GB SSD", "stock": 20, "image_url": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f8f9fa'/%3E%3Ctext x='150' y='90' text-anchor='middle' font-family='Arial' font-size='14' fill='%23333'%3EDell XPS 13%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' font-family='Arial' font-size='16' font-weight='bold' fill='%23059669'%3E$1299.99%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'%3ELaptop%3C/text%3E%3C/svg%3E"},
        {"name": "HP Pavilion 15", "category": "laptop", "price": 699.99, "description": "Budget-friendly laptop with AMD Ryzen 5, 8GB RAM, 256GB SSD", "stock": 25, "image_url": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f8f9fa'/%3E%3Ctext x='150' y='90' text-anchor='middle' font-family='Arial' font-size='14' fill='%23333'%3EHP Pavilion 15%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' font-family='Arial' font-size='16' font-weight='bold' fill='%23059669'%3E$699.99%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'%3ELaptop%3C/text%3E%3C/svg%3E"},
        {"name": "Lenovo ThinkPad X1", "category": "laptop", "price": 1899.99, "description": "Business laptop with Intel i7, 16GB RAM, 1TB SSD", "stock": 12, "image_url": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f8f9fa'/%3E%3Ctext x='150' y='90' text-anchor='middle' font-family='Arial' font-size='14' fill='%23333'%3ELenovo ThinkPad X1%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' font-family='Arial' font-size='16' font-weight='bold' fill='%23059669'%3E$1899.99%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'%3ELaptop%3C/text%3E%3C/svg%3E"},
        {"name": "ASUS ROG Strix", "category": "laptop", "price": 1599.99, "description": "Gaming laptop with RTX 3070, 16GB RAM, 512GB SSD", "stock": 8, "image_url": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23f8f9fa'/%3E%3Ctext x='150' y='90' text-anchor='middle' font-family='Arial' font-size='14' fill='%23333'%3EASUS ROG Strix%3C/text%3E%3Ctext x='150' y='110' text-anchor='middle' font-family='Arial' font-size='16' font-weight='bold' fill='%23059669'%3E$1599.99%3C/text%3E%3Ctext x='150' y='130' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'%3ELaptop%3C/text%3E%3C/svg%3E"},
        
        # Phones
        {"name": "iPhone 14 Pro", "category": "phone", "price": 999.99, "description": "Latest iPhone with A16 chip, 128GB storage, Pro camera system", "stock": 30, "image_url": "https://picsum.photos/300/200?random=6"},
        {"name": "Samsung Galaxy S23", "category": "phone", "price": 799.99, "description": "Android flagship with Snapdragon 8 Gen 2, 256GB storage", "stock": 25, "image_url": "https://picsum.photos/300/200?random=7"},
        {"name": "Google Pixel 7", "category": "phone", "price": 599.99, "description": "Pure Android experience with excellent camera, 128GB storage", "stock": 20, "image_url": "https://picsum.photos/300/200?random=8"},
        {"name": "OnePlus 11", "category": "phone", "price": 699.99, "description": "Fast charging phone with Snapdragon 8 Gen 2, 256GB storage", "stock": 18, "image_url": "https://picsum.photos/300/200?random=9"},
        {"name": "Xiaomi Mi 13", "category": "phone", "price": 549.99, "description": "Value flagship with Snapdragon 8 Gen 2, 256GB storage", "stock": 22, "image_url": "https://picsum.photos/300/200?random=10"},
          # Tablets
        {"name": "iPad Pro 12.9", "category": "tablet", "price": 1099.99, "description": "Professional tablet with M2 chip, 128GB storage, Apple Pencil support", "stock": 15, "image_url": "https://picsum.photos/300/200?random=11"},
        {"name": "Samsung Galaxy Tab S8", "category": "tablet", "price": 699.99, "description": "Android tablet with S Pen, 128GB storage, 11-inch display", "stock": 18, "image_url": "https://picsum.photos/300/200?random=12"},
        {"name": "Microsoft Surface Pro 9", "category": "tablet", "price": 999.99, "description": "2-in-1 tablet with Intel i5, 256GB SSD, Type Cover included", "stock": 12, "image_url": "https://picsum.photos/300/200?random=13"},
        {"name": "iPad Air", "category": "tablet", "price": 599.99, "description": "Lightweight tablet with M1 chip, 64GB storage, 10.9-inch display", "stock": 20, "image_url": "https://picsum.photos/300/200?random=14"},
          # Headphones
        {"name": "AirPods Pro 2", "category": "headphone", "price": 249.99, "description": "Wireless earbuds with active noise cancellation, spatial audio", "stock": 40, "image_url": "https://picsum.photos/300/200?random=15"},
        {"name": "Sony WH-1000XM5", "category": "headphone", "price": 399.99, "description": "Over-ear headphones with industry-leading noise cancellation", "stock": 25, "image_url": "https://picsum.photos/300/200?random=16"},
        {"name": "Bose QuietComfort 45", "category": "headphone", "price": 329.99, "description": "Comfortable noise-canceling headphones with 24-hour battery", "stock": 20, "image_url": "https://picsum.photos/300/200?random=17"},
        {"name": "Sennheiser HD 660S", "category": "headphone", "price": 499.99, "description": "Open-back audiophile headphones with natural sound", "stock": 15, "image_url": "https://picsum.photos/300/200?random=18"},
        {"name": "Beats Studio3", "category": "headphone", "price": 199.99, "description": "Wireless headphones with Apple W1 chip, 22-hour battery", "stock": 30, "image_url": "https://picsum.photos/300/200?random=19"},
          # Cameras
        {"name": "Canon EOS R5", "category": "camera", "price": 3899.99, "description": "Full-frame mirrorless camera with 45MP sensor, 8K video", "stock": 5, "image_url": "https://picsum.photos/300/200?random=20"},
        {"name": "Sony A7 IV", "category": "camera", "price": 2499.99, "description": "Full-frame mirrorless with 33MP sensor, 4K video", "stock": 8, "image_url": "https://picsum.photos/300/200?random=21"},
        {"name": "Nikon Z6 II", "category": "camera", "price": 1999.99, "description": "Full-frame mirrorless with dual processors, excellent low light", "stock": 6, "image_url": "https://picsum.photos/300/200?random=22"},
        {"name": "Fujifilm X-T5", "category": "camera", "price": 1699.99, "description": "APS-C mirrorless with 40MP X-Trans sensor, film simulations", "stock": 10, "image_url": "https://picsum.photos/300/200?random=23"},
        {"name": "GoPro Hero 11", "category": "camera", "price": 399.99, "description": "Action camera with 5.3K video, waterproof, image stabilization", "stock": 25, "image_url": "https://picsum.photos/300/200?random=24"},
        
        # Speakers
        {"name": "HomePod mini", "category": "speaker", "price": 99.99, "description": "Smart speaker with Siri, spatial audio, HomeKit hub", "stock": 35, "image_url": "https://picsum.photos/300/200?random=25"},
        {"name": "Amazon Echo Dot", "category": "speaker", "price": 49.99, "description": "Compact smart speaker with Alexa, great sound", "stock": 50, "image_url": "https://picsum.photos/300/200?random=26"},
        {"name": "JBL Charge 5", "category": "speaker", "price": 179.99, "description": "Portable Bluetooth speaker with powerbank, IP67 waterproof", "stock": 30, "image_url": "https://picsum.photos/300/200?random=27"},
        {"name": "Sonos One", "category": "speaker", "price": 199.99, "description": "Smart speaker with Alexa and Google Assistant, rich sound", "stock": 20, "image_url": "https://picsum.photos/300/200?random=28"},
        {"name": "Bose SoundLink Revolve", "category": "speaker", "price": 149.99, "description": "360-degree Bluetooth speaker with 12-hour battery", "stock": 25, "image_url": "https://picsum.photos/300/200?random=29"},
        
        # Gaming Accessories
        {"name": "PlayStation 5", "category": "gaming", "price": 499.99, "description": "Next-gen gaming console with ultra-high speed SSD", "stock": 3, "image_url": "https://picsum.photos/300/200?random=30"},
        {"name": "Xbox Series X", "category": "gaming", "price": 499.99, "description": "Most powerful Xbox with 4K gaming, Quick Resume", "stock": 5, "image_url": "https://picsum.photos/300/200?random=31"},
        {"name": "Nintendo Switch OLED", "category": "gaming", "price": 349.99, "description": "Handheld console with vibrant OLED screen", "stock": 15, "image_url": "https://picsum.photos/300/200?random=32"},
        {"name": "Razer DeathAdder V3", "category": "gaming", "price": 89.99, "description": "Ergonomic gaming mouse with Focus Pro sensor", "stock": 40, "image_url": "https://picsum.photos/300/200?random=33"},
        {"name": "Corsair K95 RGB", "category": "gaming", "price": 199.99, "description": "Mechanical gaming keyboard with Cherry MX switches", "stock": 20, "image_url": "https://picsum.photos/300/200?random=34"},
        
        # Smart Home
        {"name": "Nest Thermostat", "category": "smart-home", "price": 129.99, "description": "Smart thermostat with energy saving features", "stock": 25, "image_url": "https://picsum.photos/300/200?random=35"},
        {"name": "Ring Video Doorbell", "category": "smart-home", "price": 179.99, "description": "Smart doorbell with HD video, two-way talk", "stock": 30, "image_url": "https://picsum.photos/300/200?random=36"},
        {"name": "Philips Hue Starter Kit", "category": "smart-home", "price": 199.99, "description": "Smart lighting system with millions of colors", "stock": 15, "image_url": "https://picsum.photos/300/200?random=37"},
        {"name": "TP-Link Kasa Smart Plug", "category": "smart-home", "price": 24.99, "description": "WiFi smart plug with voice control, scheduling", "stock": 60, "image_url": "https://picsum.photos/300/200?random=38"},
        
        # Accessories
        {"name": "Anker PowerCore 10000", "category": "accessory", "price": 29.99, "description": "Portable charger with 10000mAh capacity, fast charging", "stock": 100, "image_url": "https://picsum.photos/300/200?random=39"},
        {"name": "SanDisk Ultra 128GB", "category": "accessory", "price": 19.99, "description": "High-speed USB 3.0 flash drive with 128GB storage", "stock": 80, "image_url": "https://picsum.photos/300/200?random=40"},
        {"name": "Belkin USB-C Hub", "category": "accessory", "price": 79.99, "description": "7-in-1 USB-C hub with HDMI, USB-A, SD card slots", "stock": 35, "image_url": "https://picsum.photos/300/200?random=41"},
        {"name": "Apple MagSafe Charger", "category": "accessory", "price": 39.99, "description": "Wireless charger for iPhone with magnetic alignment", "stock": 45, "image_url": "https://picsum.photos/300/200?random=42"},
        {"name": "Samsung 25W Fast Charger", "category": "accessory", "price": 24.99, "description": "USB-C fast charger compatible with Samsung devices", "stock": 50, "image_url": "https://picsum.photos/300/200?random=43"},
        
        # Monitors
        {"name": "LG UltraWide 34\"", "category": "monitor", "price": 599.99, "description": "34-inch ultrawide monitor with QHD resolution, USB-C", "stock": 12, "image_url": "https://picsum.photos/300/200?random=44"},
        {"name": "Dell 4K 27\"", "category": "monitor", "price": 399.99, "description": "27-inch 4K monitor with IPS panel, color accuracy", "stock": 18, "image_url": "https://picsum.photos/300/200?random=45"},
        {"name": "ASUS Gaming 24\"", "category": "monitor", "price": 299.99, "description": "24-inch gaming monitor with 144Hz refresh rate", "stock": 20, "image_url": "https://picsum.photos/300/200?random=46"},
        {"name": "Apple Studio Display", "category": "monitor", "price": 1599.99, "description": "27-inch 5K Retina display with built-in camera", "stock": 5, "image_url": "https://picsum.photos/300/200?random=47"},
        
        # Storage
        {"name": "WD Black SN850X 1TB", "category": "storage", "price": 149.99, "description": "High-performance NVMe SSD for gaming and creative work", "stock": 25, "image_url": "https://picsum.photos/300/200?random=48"},
        {"name": "Seagate Backup Plus 2TB", "category": "storage", "price": 89.99, "description": "Portable external hard drive with USB 3.0", "stock": 30, "image_url": "https://picsum.photos/300/200?random=49"},
        {"name": "Samsung T7 Portable SSD", "category": "storage", "price": 119.99, "description": "Compact external SSD with 1TB capacity, USB-C", "stock": 28, "image_url": "https://picsum.photos/300/200?random=50"},
        
        # Networking
        {"name": "ASUS AX6000 Router", "category": "networking", "price": 349.99, "description": "WiFi 6 router with tri-band, gaming acceleration", "stock": 15, "image_url": "https://picsum.photos/300/200?random=51"},
        {"name": "TP-Link Mesh System", "category": "networking", "price": 199.99, "description": "Whole home mesh WiFi system with 3 units", "stock": 20, "image_url": "https://picsum.photos/300/200?random=52"},
        {"name": "Netgear Nighthawk", "category": "networking", "price": 149.99, "description": "AC1900 WiFi router with high-power amplifiers", "stock": 25, "image_url": "https://picsum.photos/300/200?random=53"}
    ]
    
    # Add all products to database
    for product_data in products_data:
        product = Product(**product_data)
        db.session.add(product)
    
    # Create a test user
    test_user = User(username='testuser', email='test@example.com')
    test_user.set_password('password123')
    db.session.add(test_user)
    
    # Commit all changes
    db.session.commit()
    print(f"Created {len(products_data)} products and 1 test user")

if __name__ == '__main__':
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Create sample data
        create_sample_data()
        
        print("Database initialized successfully!")
        print("Test user credentials:")
        print("Username: testuser")
        print("Password: password123")