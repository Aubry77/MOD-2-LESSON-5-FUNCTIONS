"""This application provides functions to manage 
a shopping list, including adding items, removing items, 
and printing the list."""


from ast import main


def add_item(shopping_list, item):
    
   # Add an item to the shopping list.
    
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(shopping_list, item):
    
   # Remove an item from the shopping list.
    
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def print_list(shopping_list):
    
   # Print the shopping list.
    
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

def shopping_list_maker():
    
    # main function to interact with the shopping list.
    
    shopping_list = []
    while True:
        action = input("Choose action (add, remove, print, quit): ").lower()
        if action == "add":
            item = input("Enter item to add: ")
            add_item(shopping_list, item)
        elif action == "remove":
            item = input("Enter item to remove: ")
            remove_item(shopping_list, item)
        elif action == "print":
            print_list(shopping_list)
        elif action == "quit":
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    shopping_list_maker()
