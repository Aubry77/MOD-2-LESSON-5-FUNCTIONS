"""This application is a practice exercise for creating and using sets in
 Python. The application will create two sets of inventory items and 
 perform various set operations on them. The application will then
   display the results of the set operations to the user."""


# Create lists of inventory items, caategories,
# user input for product count


#use loops to iterate through the lists and add the items to the sets

# Define the product names and categories
products = [
    ("Men's Cotton Tee", "Clothing"),
    ("Pine-Sol", "Household Goods"),
    ("Bronzer", "Household Goods"),
    ("Dawn Dish Liquid", "Household Goods"),
    ("Bluetooth Speaker", "Electronics"),
    ("Barbie Doll", "Toys"),
    ("Comet", "Household Goods"),
    ("Match Box Cars", "Toys"),
    ("Legos", "Toys")
]

# Remove duplicates
unique_products = list(set(products))

# Organize products into a dictionary by category
inventory = {
    "Toys": [],
    "Household Goods": [],
    "Electronics": [],
    "Clothing": []
}

# Populate the inventory dictionary
#use try except block to handle errors
for product, category in unique_products:
    try:
        inventory[category].append(product)
    except KeyError:
        print(f"Category {category} does not exist.")

# Function to get product count from user
def get_product_count():
    while True:
        try:
            count = int(input("Enter the number of products you want to add: "))
            return count
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to display inventory and get user input
def main():
    print("Current Inventory:")
    for category, items in inventory.items():
        print(f"{category}:")
        for item in items:
            print(f" - {item}")
        print()

    count = get_product_count()
    print(f"You want to add {count} products.")

if __name__ == "__main__":
    main()


