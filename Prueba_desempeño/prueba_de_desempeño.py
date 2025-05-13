# Dictionary to store inventory {name: (price, quantity)}
store = {}
# We make the add_product function to validate and ask the user for the product data to add
def add_product():
    name_product = input("Enter your product: ")
    if name_product in store:
       print("¡This product already exists!")
       return
   
    try:
        price = float(input("Enter the price of your product: "))
        quantity = int(input("Enter the quantity of your product you wish to take: "))
        
        if price <=0 or quantity <0:
            print("!Price and quantity must be positive values¡")
            return
        store [name_product] = (price, quantity)
        print(f"Product '{name_product}' add correctly")
    except:
        print("Values invalid")

# Function to search for product and condition if the product is the same
def search_product():
    name_product = input("Enter the name to search for : ")
    
    if name_product in store:
        price, quanlity = store[name_product]
        print(f"\nProduct: {name_product}")
        print(f"Price: ${price:.2f}")
        print(f"Quantily available: {quanlity}")
    else:
        print("¡Product not found in inventory!")
        

#Function for update the price on product
def update_price():
    name_product = input("Enter the name of the product to update: ")
    
    if name_product not in store:
        print("¡Product not found!")
        return
    
    try:
        new_price = float(input("Enter the new price: "))
        if new_price <= 0:
            print("¡Error! The price must be positive values")
            return
            
        # We only update the price, keeping the quantity
        quanlity = store[name_product][1]
        store[name_product] = (new_price, quanlity)
        print(f"Price the '{name_product}' update correctly")
    except:
        print("¡Error! Enter a valid numeric value for the price")

# Function to delete a product
def delete_product():
    name_product = input("Enter the name of the product to detele: ")
    yes = "Y"
    no = "N"
    condition = input(f"If you want to delete the product ({yes}) or do not want to delete it ({no}):")
    #We use a conditional to confirm whether the user is sure to study the product
    if condition == yes:
        print("keep going")
        if name_product in store:
            del store[name_product]
            print(f"Product '{name_product}' detele correctly")
        else:
            print("¡Product no found!")
    elif condition== no:
        print("keep going no completed")
    else:
        print("It has to be a capital Y and a capital N")

# Function for quantly the valid total in inventory
def calculate_valued_total():
    # We use a lambda function to calculate the value per product
    calculate_valued = lambda item: item[1][0] * item[1][1]
    
    if not store:
        print("The inventory is empty")
        return
    
    print("\n--- PRODUCT ON INVENTORY ---")
    for name_product, (preci, quantly) in store.items():
            print(f"{name_product}: {quantly} units ${preci:.2f}")
    
    total = sum(calculate_valued(item) for item in store.items())
    print(f"\nTotal inventory value: ${total:.2f}")
    print(f"Number of different products: {len(store)}")

# Main function that handles the menu
while True:
    print("\n--- INVENTORY MANAGEMENT ---")
    print("1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Exit")
        
    opcion = input("Select one option (1-6): ")
        
    if opcion == "1":
        add_product()
    elif opcion == "2":
        search_product()
    elif opcion == "3":
        update_price()
    elif opcion == "4":
        delete_product()
    elif opcion == "5":
        calculate_valued_total()
    elif opcion == "6":
        print("Leaving the system...")
        break
    else:
        print("Invalid option. Please try again")
