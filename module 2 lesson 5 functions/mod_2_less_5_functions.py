"""
This module provides basic arithmetic operations and a simple calculator function.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    try:
        operation = input("Choose operation (add, subtract, multiply, divide): ").lower()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "add":
            print(f"The result is: {add(num1, num2)}")
        elif operation == "subtract":
            print(f"The result is: {subtract(num1, num2)}")
        elif operation == "multiply":
            print(f"The result is: {multiply(num1, num2)}")
        elif operation == "divide":
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    calculator()


"""
This application provides functions to manage a shopping list, including adding items, removing items, and printing the list.
"""

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def print_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

def shopping_list_manager():
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
            print("Invalid action!")

# Example usage
if __name__ == "__main__":
    shopping_list_manager()