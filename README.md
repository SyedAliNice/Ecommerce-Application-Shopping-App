
# Shopping App Backend
#   Overview

This is a simple shopping application backend implemented in Python. The application provides functionalities for both regular users and administrators, including product browsing, cart management, checkout, and catalog management.

#   Features
#   User Features
1.  Login System: Secure user authentication with username/password
2.  Product Catalog: View available products with details (ID, name, category, price)
#   Cart Management:
1.  Add products to cart
2.  Remove products from cart 
3.  View cart contents
#   Checkout Process:
1.  Multiple payment methods (UPI, Debit/Credit Card, Net Banking)
2.  Order summary display
3.  Automatic cart clearing after checkout
#   Admin Features
#   Catalog Management:
1.  Add new products
2.  Modify existing products
3.  Remove products
#   Category Management:
1.  Add new categories
2.  Remove unused categories
#   Data Structures
#   Databases
1.  users_db: Stores user credentials (username: password)
2.  admin_db: Stores admin credentials (username: password)
3.  demo_sessions: Tracks active user sessions
4.  product_catalog: Stores all available products
5.  categories: Stores product categories
6.  user_cart: Tracks each user's shopping cart items
#   Product Structure
Each product contains:
1.  product_id: Unique identifier
2.  name: Product name
3.  category_id: Reference to category
4.  price: Product price in rupees
#   How to Run
1.  Ensure you have Python installed (Python 3.x recommended)
2.  Run the application by executing: python main.py
3.  Follow the on-screen prompts to login and use the application
#   Usage Examples
#   As a User
1.  Login with username "user1" and password "password1"
2.  Browse products (Option 1)
3.  Add products to cart (Option 3)
4.  View cart (Option 2)
5.  Checkout when ready (Option 5)
#   As an Admin
1.  Login with username "admin" and password "adminpass"
2.  View current catalog (Option 1)
3.  Add new products (Option 2)
4.  Modify existing products (Option 3)
5.  Manage categories (Options 5-6)
#   Demo Credentials
#   Users:
1.  user1 / password1
2.  user2 / password2
#   Admin:
1.  admin / adminpass





