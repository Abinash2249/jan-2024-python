
# Write a program which takes radius as an input and calculate the area of the circle.  Pi*r**2

radius = int(input("Enter a number: "))
area_of_circle = 22/7 * radius **2
print(area_of_circle)

# Write a program to find the frequency of the input number in a list
# [5, 2, 3, 5, 3, 2, 3, 3, 1, 4]


Numbers = [5,2,3,5,3,2,3,3,1,4]
num1 = int(input("Enter a number: "))
result = Numbers.count(num1)
print(f"The frequency of the {num1} is {result}.")

