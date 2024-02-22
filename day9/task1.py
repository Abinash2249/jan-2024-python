# WAP to take a number input. If the number is divisible by 3 print "fizz", if divisible by 5, print "buzz"
# If divisible by both 3 and 5 print "fizzbuzz". If not divisible by both 3 and 5 then print the number as it is


num1 = int(input("Enter a number: "))
if num1%3 == 0 and num1%5 ==0:
    print("fizzbuzz")
elif num1%3 == 0:
    print("fizz")
elif num1%5 == 0:
    print("buzz")
else:
    print(num1)



