# Student: Valentina Hernandez Vera
# Additional features: Personalized the experience a little bit more by adding a greeting\introduction and asking the customer's name and address.

print("Welcome to OnlineFood! This program serves to verify the prices of the meals you already selected. It will not take longer than a few minutes.")
print("We will also ask you a few things that will let us know who to deliver the food to and where.")

customer = input("First things first, What is your first name? ")
address = input("Thank you! Now, where do you want to receive your order? Please state the address: ")

print("Thank you! Now, let's get to the prices.")

child_meal = input("What is the price of a child's meal? $")
adult_meal = input("What is the price of an adult's meal? $")
child_num = input("How many children are there? ")
adult_num = input("How many adults are there? ")

subtotal = (int(child_num) * float(child_meal)) + (int(adult_num) * float(adult_meal))

print(f"Subtotal: ${subtotal:.2f}")

tax_rate = float(input("What is the sales tax rate of your area? "))
tax_price = (float(subtotal) * tax_rate) / 100
print(f"Sales Tax: {tax_price:.2f}%")
total = float(tax_price) + float(subtotal)
print(f"Total: ${total:.2f}")

payment = input("What is the payment amount? ")
change = float(payment) - float(total)
print(f"Change: ${change:.2f}")

print(f"Thank you, {customer.capitalize()}! Your order will be ready soon. It will be delivered to: {address.title()}.")