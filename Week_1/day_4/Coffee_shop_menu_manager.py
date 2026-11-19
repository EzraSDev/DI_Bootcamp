menu_dict = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}
order = []

def show_menu(menu_dict):
    if menu_dict:
        print("Menu:")
        for drink, price in menu_dict.items():
            print(f"{drink}: ${price:.2f}")
    else:
        print("The menu is empty.")



def add_item(menu_dict):
    """Add a new drink to the menu."""
    input_drink = input("Enter the name of the drink to add: ")
    input_price = float(input("Enter the price of the drink: "))
    if input_drink in menu_dict:
        print(f"{input_drink} is already on the menu.")
    else:
        menu_dict[input_drink] = input_price
        print(f"{input_drink} has been added to the menu with a price of ${input_price:.2f}.")


def update_price(menu_dict):
    print("Do you want to update the price of an existing drink? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        input_drink = input("Enter the name of the drink you want to update: ")
        if input_drink in menu_dict:
            new_price = float(input("Enter the new price: "))
            menu_dict[input_drink] = new_price
            print(f"The price of {input_drink} has been updated to ${new_price:.2f}.")
        else:
            print(f"{input_drink} is not on the menu.")
    else:
        print("No changes made.")

def delete_item(menu_dict):
    input_drink = input("Enter the name of the drink to delete: ")
    if input_drink in menu_dict:
        del menu_dict[input_drink]
        print(f"{input_drink} has been removed from the menu.")
    else:
        print(f"{input_drink} is not on the menu.")


def show_options(menu_dict):

    print("What would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")
    


def run_coffee_shop():
    """Main loop of the program."""
    # TODO
    show_options()
    while True:
        input_choice = input("Enter your choice (1-5): ")
        if input_choice == "1":
            show_menu(menu_dict)
        elif input_choice == "2":
            add_item(menu_dict)
        elif input_choice == "3":
            update_price(menu_dict)
        elif input_choice == "4":
            delete_item(menu_dict)
        elif input_choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        show_options()
     
    
run_coffee_shop()
