
import sys


# This code snippet is a simple shopping list manager that allows the user to add, remove, print, and clear items from a list.
# The user is prompted to enter an item and then choose an action by entering a number.
shopping_list = []
choice = ""
# print(shopping_list)

while choice != "5":
    choice = input('Choose an action: 1 to add, 2 to remove, 3 to print, 4 to clear, 5 to exit: ')
    
    if not (choice.isdigit() and 1 <= int(choice) <= 5):
        print("Invalid action. Please enter a number between 1 and 5.")
        continue
    choice = int(choice)
    if choice == 1:
        item = input('Enter an item: ')
        if item not in shopping_list:
            shopping_list.append(item.lower())
        # shopping_list = set(shopping_list)
        
            print(f"The item {item} was added")
            print(shopping_list)
    
    elif choice == 2:
        item = input('Enter an item: ')
        if item in shopping_list:
            shopping_list.remove(item.lower())
            print(f"The item {item} was removed")
        else:
            print("Item not found in the list.")
    
    elif choice == 3:
        if shopping_list:
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("The list is empty.")
    
    elif choice == 4:
        shopping_list.clear()
        print("List cleared.")
    
    elif choice == 5:
        print("Exiting the program.")
        sys.exit()   

# first = x.append(a)
# second = x.remove(a)
# third = print(x)
# fourth = x.clear()
# print(xi