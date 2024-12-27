class ShoppingList:
    
    """
   In this application I am using A class to represent a shopping list.
   parameters: items (list): A list to store shopping items.
    """
    

    def __init__(self):
        
    # Initializes a new shopping list with an empty list of items.
    
        self.items = []

    def add_item(self, item):
        
       # Adds an item to the shopping list.

        # Parameters item (str): The item to add to the list.
        
        self.items.append(item)

    def remove_item(self, item):
        
       # Removes an item from the shopping list.

       # Parameters: item (str): The item to remove from the list.
        
        if item in self.items:
            self.items.remove(item)

    def print_list(self):
        
       # Prints the shopping list in a formatted way.
        
        print("Shopping List:")
        for item in self.items:
            print(f"- {item}")

# Example usage:

if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Apples")
    shopping_list.add_item("Bread")
    shopping_list.print_list()
    shopping_list.remove_item("Apples")
    shopping_list.print_list()