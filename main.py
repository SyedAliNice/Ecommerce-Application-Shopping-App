# Shopping App Backend Implementation

import uuid  # For generating session IDs

# Demo databases for users and admin
users_db = {
    "user1": "password1",
    "user2": "password2",
}

admin_db = {
    "admin": "adminpass",
}

# Session tracking
demo_sessions = {}

# Dummy product catalog and categories
product_catalog = [
    {"product_id": 1, "name": "Running Shoes", "category_id": 1, "price": 2000},
    {"product_id": 2, "name": "Winter Jacket", "category_id": 2, "price": 5000},
    {"product_id": 3, "name": "Smartphone", "category_id": 3, "price": 15000},
    {"product_id": 4, "name": "Baseball Cap", "category_id": 2, "price": 500},
]

categories = {
    1: "Footwear",
    2: "Clothing",
    3: "Electronics"
}

# User carts
user_cart = {}

# Welcome message
def welcome_message():
    print("Welcome to the Demo Marketplace")

# View catalog
def view_catalog():
    print("\nProduct Catalog:")
    print(f"{'Product ID':<10}{'Name':<20}{'Category':<15}{'Price':<10}")
    print("-" * 55)
    for product in product_catalog:
        category_name = categories.get(product["category_id"], "Unknown")
        print(f"{product['product_id']:<10}{product['name']:<20}{category_name:<15}{product['price']:<10}")

# Cart management functions
def view_cart(session_id):
    print("\nYour Cart:")
    if session_id not in user_cart or not user_cart[session_id]:
        print("Your cart is empty.")
        return
    print(f"{'Product ID':<10}{'Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)
    total_price = 0
    for item in user_cart[session_id]:
        print(f"{item['product_id']:<10}{item['name']:<20}{item['quantity']:<10}{item['price']:<10}")
        total_price += item['price'] * item['quantity']
    print(f"\nTotal Price: {total_price}")

def add_to_cart(session_id):
    product_id = int(input("Enter the Product ID to add to cart: "))
    quantity = int(input("Enter the quantity: "))
    
    product = next((item for item in product_catalog if item["product_id"] == product_id), None)
    if product:
        if session_id not in user_cart:
            user_cart[session_id] = []
        user_cart[session_id].append({"product_id": product["product_id"], 
                                      "name": product["name"], 
                                      "quantity": quantity, 
                                      "price": product["price"]})
        print(f"{quantity} x {product['name']} added to your cart.")
    else:
        print("Invalid Product ID.")

def remove_from_cart(session_id):
    product_id = int(input("Enter the Product ID to remove from cart: "))
    if session_id in user_cart:
        cart_items = user_cart[session_id]
        product = next((item for item in cart_items if item["product_id"] == product_id), None)
        if product:
            user_cart[session_id].remove(product)
            print(f"{product['name']} removed from your cart.")
        else:
            print("Product not found in your cart.")
    else:
        print("Your cart is empty.")

# Payment checkout function
def checkout(session_id):
    if session_id not in user_cart or not user_cart[session_id]:
        print("Your cart is empty. Please add items to your cart before checkout.")
        return
    
    # Calculate total price
    total_price = sum(item['price'] * item['quantity'] for item in user_cart[session_id])
    
    # Display cart summary
    print("\nCheckout Summary:")
    print(f"{'Product ID':<10}{'Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)
    for item in user_cart[session_id]:
        print(f"{item['product_id']:<10}{item['name']:<20}{item['quantity']:<10}{item['price']:<10}")
    print(f"\nTotal Price: {total_price}")
    
    # Payment method selection
    print("\nSelect Payment Method:")
    print("1. UPI")
    print("2. Debit/Credit Card")
    print("3. Net Banking")
    payment_choice = input("Enter your choice (1/2/3): ")
    
    if payment_choice == "1":
        print(f"Your order is successfully placed. Please complete the payment of Rs. {total_price} through UPI.")
    elif payment_choice == "2":
        print(f"Thank you for choosing Debit/Credit Card. Your payment of Rs. {total_price} is being processed.")
    elif payment_choice == "3":
        print(f"Thank you for choosing Net Banking. Please complete the payment of Rs. {total_price}.")
    else:
        print("Invalid payment method selected. Returning to menu.")
        return
    
    # Clear the cart after checkout
    user_cart[session_id] = []
    print("Your cart has been cleared. Thank you for shopping with us!")

# Admin functionalities for catalog management
def add_product():
    name = input("Enter product name: ")
    category_id = int(input("Enter category ID (1. Footwear, 2. Clothing, 3. Electronics): "))
    price = int(input("Enter product price: "))
    product_id = max([product["product_id"] for product in product_catalog]) + 1  # Auto-generate ID
    product_catalog.append({"product_id": product_id, "name": name, "category_id": category_id, "price": price})
    print(f"Product '{name}' added successfully!")

def modify_product():
    product_id = int(input("Enter Product ID to modify: "))
    product = next((item for item in product_catalog if item["product_id"] == product_id), None)
    if product:
        print(f"Current details: Name = {product['name']}, Category = {categories[product['category_id']]}, Price = {product['price']}")
        name = input("Enter new product name (leave blank to keep current): ")
        category_id = input("Enter new category ID (1. Footwear, 2. Clothing, 3. Electronics, leave blank to keep current): ")
        price = input("Enter new price (leave blank to keep current): ")

        if name:
            product['name'] = name
        if category_id:
            # Only update category_id if input is not empty
            if category_id.isdigit():
                product['category_id'] = int(category_id)
        if price:
            # Only update price if input is not empty
            if price.isdigit():
                product['price'] = int(price)
        print("Product updated successfully!")
    else:
        print("Product not found.")


def remove_product():
    product_id = int(input("Enter Product ID to remove: "))
    product = next((item for item in product_catalog if item["product_id"] == product_id), None)
    if product:
        product_catalog.remove(product)
        print(f"Product '{product['name']}' removed successfully!")
    else:
        print("Product not found.")

def add_category():
    category_name = input("Enter new category name: ")
    category_id = max(categories.keys()) + 1  # Auto-generate category ID
    categories[category_id] = category_name
    print(f"Category '{category_name}' added successfully!")

def remove_category():
    category_id = int(input("Enter Category ID to remove: "))
    if category_id in categories:
        if any(product["category_id"] == category_id for product in product_catalog):
            print("Category is in use. Please reassign products before removal.")
        else:
            del categories[category_id]
            print(f"Category '{categories[category_id]}' removed successfully!")
    else:
        print("Category not found.")

# Modified user menu in the login function
def login():
    print("\nLogin as:")
    print("1. User")
    print("2. Admin")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users_db and users_db[username] == password:
            session_id = str(uuid.uuid4())
            demo_sessions[session_id] = {"role": "user", "username": username}
            print(f"User login successful! Your session ID: {session_id}")
            # User menu after login
            while True:
                print("\n1. View Catalog")
                print("2. View Cart")
                print("3. Add Items to Cart")
                print("4. Remove Items from Cart")
                print("5. Checkout")
                print("6. Logout")
                user_choice = input("Enter your choice: ")
                
                if user_choice == "1":
                    view_catalog()
                elif user_choice == "2":
                    view_cart(session_id)
                elif user_choice == "3":
                    add_to_cart(session_id)
                elif user_choice == "4":
                    remove_from_cart(session_id)
                elif user_choice == "5":
                    checkout(session_id)
                elif user_choice == "6":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid username or password.")
    
    elif choice == "2":
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        
        if admin_username in admin_db and admin_db[admin_username] == admin_password:
            print("Admin login successful!")
            # Admin functionalities after login
            while True:
                print("\n1. View Catalog")
                print("2. Add Product")
                print("3. Modify Product")
                print("4. Remove Product")
                print("5. Add Category")
                print("6. Remove Category")
                print("7. Logout")
                admin_choice = input("Enter your choice: ")
                
                if admin_choice == "1":
                    view_catalog()
                elif admin_choice == "2":
                    add_product()
                elif admin_choice == "3":
                    modify_product()
                elif admin_choice == "4":
                    remove_product()
                elif admin_choice == "5":
                    add_category()
                elif admin_choice == "6":
                    remove_category()
                elif admin_choice == "7":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid admin username or password.")
    else:
        print("Invalid choice. Please try again.")


# Start the application
if __name__ == "__main__":
    welcome_message()
    login()
