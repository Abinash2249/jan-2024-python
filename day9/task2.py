
# Find the greatest among three numbers

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number > second_number and first_number > third_number:
    print(f"The greatest number is {first_number}, first number.")
elif second_number>first_number and second_number> third_number:
    print(f"The greatest number is {second_number}, second number.")
elif third_number > first_number and third_number> second_number:
    print(f"The greatest number is {third_number}, third number")

