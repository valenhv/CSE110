numbers_list = []
print("Enter a list of numbers. Type 0 when you're finished.")
number = ""
while number != 0:
    number = float(input("Enter a number: "))
    numbers_list.append(number)
print(f"The sum is: {sum(numbers_list)}")
average = sum(numbers_list)/len(numbers_list)
print(f"The average is: {average}")
print(f"The smallest number is: {min(numbers_list)}")
print(f"The largest number is: {max(numbers_list)}")