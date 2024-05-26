# Student: Valentina Hernandez Vera
# Creativity: Used "import os" to clear the console after every action and let the user press enter so they can read what the program says before it clears, also used "try" and "exceptValueError" to detect an invalid input.
import os

shopping_list = []
price_list = []

running_total = 0

options_numbers = [1, 2, 3, 4, 5]
options_list = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

print("Welcome to the Shopping Cart Program!")

user_action = 0

while True:
    try:
        print("**MENU**")
        print("Select an option with its corresponding number.")
        for i in range(len(options_list)):
            option = options_list[i]
            number = options_numbers[i]
            print(f"{number}. {option}")
        user_action = int(input(">>"))
        os.system('cls')
        
        if user_action == 1:
            print("**ADD ITEM**")
            print("What item would you like to add?")
            add_item = input(">>")
            shopping_list.append(add_item)
            print(f"What is the price of '{add_item}'?")
            add_price = float(input(">>$"))
            price_list.append(add_price)
            print(f"'{add_item.capitalize()}' has been added to the cart.")
            input("Press Enter to go back to the menu.")
            
        elif user_action == 2:
            print("**SHOPPING CART**")
            print("The contents of the shopping cart are:")
            for i in range(0, len(shopping_list)):
                item = shopping_list[i]
                price = price_list[i]
                number = i+1
                print(f"{number}. {item.capitalize()} - ${price:.2f}")
            input("Press Enter to go back to the menu.")

        elif user_action == 3:
            print("**REMOVE ITEM**")
            print("Which one of these would you like to remove?")
            for i in range(0, len(shopping_list)):
                item = shopping_list[i]
                price = price_list[i]
                number = i+1
                print(f"{number}. {item.capitalize()} - ${price:.2f}")
            print("Insert the ID number of the item you would like to remove.")
            removed_item = int(input(">>"))
            real_index = removed_item - 1
            del shopping_list[real_index]
            del price_list[real_index]
            print("Item removed succesfully!")
            input("Press Enter to go back to the menu.")

        elif user_action == 4:
            print("**COMPUTE TOTAL**")
            print("This is your shopping list, the running total is below:")
            for i in range(0, len(shopping_list)):
                item = shopping_list[i]
                price = price_list[i]
                number = i+1
                print(f"{number}. {item.capitalize()} - ${price:.2f}")
            running_total = sum(price_list)
            print(f"TOTAL: ${running_total:.2f}")
            input("Press Enter to go back to the menu.")

        elif user_action == 5:
            break

        else:
            print("Invalid option. Please enter a number from 1 to 5.")
        os.system('cls')

    except ValueError:
        print("Invalid input. Please enter an integer.")


print("Thank you for using our services. Goodbye!")