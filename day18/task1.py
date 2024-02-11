# # Take two numbers as input and add those numbers. Handle the possible exceptions.


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

except ValueError:
    print("Enter valid value")

else:
    addition = a + b
    print(addition)
finally:
    print("Code was executed")

# Take two numbers input and divide a number by another number. Handle the possible exceptions.

try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 / num2

except ValueError:
    print("Enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by 0, use a different number.")

else:
    print(result)

finally:
    print("Code executed")



# Create a dictionary student with keys id, name, age, department. Take a input from the user,
# which info (id, name, age or department) he wants to access and print the result. Handle the possible exceptions.


student = {"id": 2, "name": "Jane", "age": 30, "address": "KTM"}

key = input("Enter info you want to access ")
try:
    value = student[key]
except KeyError:
    print("The info is not provided for the student")
else:
    print(f"The {key} of the student is {value}")