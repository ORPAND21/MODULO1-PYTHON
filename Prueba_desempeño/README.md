# Dictionary to store inventory {name: (price, quantity)}

# We make the add_product function to validate and ask the user for the product data to add

# Function to search for product and condition if the product is the same

# Function for update the price on product
## We only update the price, keeping the quantity

# Function to delete a product
## We use a conditional to confirm whether the user is sure to study the product

# Function for quantly the valid total in inventory
## We use a lambda function to calculate the value per product

# Main function that handles the menu



# Example with a product
## Esto se imprime en la consola 
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 6
Leaving the system...
'''
## El 1 para añadir un producto
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 1
Enter your product: chicken
Enter the price of your product: 20
Enter the quantity of your product you wish to take: 1
Product 'chicken' add correctly
'''
## 2 para busca el producto recientemente agregado
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 2
Enter the name to search for : chicken

Product: chicken
Price: $20.00
Quantily available: 1
'''
## 3 Cambiar la el precio del producto
'''
--- INVENTORY MANAGEMENT ---
    . Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 3
Enter the name of the product to update: chicken
Enter the new price: 50 
Price the 'chicken' update correctly
'''
## pasamos al 5 para que puedas verificar si se modifico el precio en el invetario
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 5

--- PRODUCT ON INVENTORY ---
chicken: 1 units $50.00

Total inventory value: $50.00
Number of different products: 1
'''
## 4 Para eliminar el producto
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 4
Enter the name of the product to detele: chicken
If you want to delete the product (Y) or do not want to delete it (N):Y
keep going
Product 'chicken' detele correctly
'''
## 6 si te quieres salir del programa 
'''
--- INVENTORY MANAGEMENT ---
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. Exit
Select one option (1-6): 6
Leaving the system...
'''