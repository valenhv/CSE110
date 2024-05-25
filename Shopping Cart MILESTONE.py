# Student: Valentina Hernandez Vera

shopping_list = []
shopping_list_numbered = []
price_list = []

running_total = 0
user_action = ""

options_numbers = [1, 2, 3, 4, 5]
options_list = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following:")

while user_action != 5:

    for i in range(len(options_list)):
        option = options_list[i]
        number = options_numbers[i]
        print(f"{number}. {option}")
    user_action = input("Please enter an action: ")

    if user_action == 1:
        print("What item would you like to add?")
        add_item = input(">>")
        shopping_list.append(add_item)
        shopping_list_numbered.append(add_item)
        print(f"What is the price of '{add_item}'?")
        add_price = input(">>")
        price_list.append(add_price)
        print(f"'{add_item.capitalize()}' has been added to the cart.")
        
    elif user_action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_list)) and range(len(shopping_list_numbered)):
            item = shopping_list[i]
            number = shopping_list_numbered[i]
            price = price_list[i]
            print(f"{number}. {item.capitalize()} - ${price:.2f}")

    elif user_action == 3:
        print("Which one of these would you like to remove?")
        for item in shopping_list:
            print(f"'{item.capitalize()}'")
        removed_item = input(">>")
    
    elif user_action == 4:
        for receipt in price_list:
            running_total += receipt
            print(f"The total is: {running_total:.2f}")

    else:
        print("Invalid input. Try again")

print("Thank you. Goodbye!")