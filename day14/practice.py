# def multiply(a,b):
#     return a*b
#
# m = multiply
# print(m(3,4))
#
#
# def addition(a,b):
#     return a+b
#
# def multiply(a,b):
#     return a*b
#
# data = [addition, multiply, 1,2,3,4,"HelloWorld"]
# print(data[0](3,4))
# print(data[1](3,5))
#
#
#
# # map()
#
# data = [1,2,3,4,5]
# #
# def to_squared(e):
#     return e**2
#
# result = map(to_squared,data)
# print(list(result))
#
#
# result = map(lambda e:e**2, data)
# print(list(result))
#
#
#
# # filter()
#
# data = ["a", "b", "c", "d", "e", "f", "g", "h"]
#
#
# def pick_vowel(each):
#     return each in ["a", "e", "i", "o", "u"]
#
# result = filter(pick_vowel, data)
# print(list(result))
#
#
# result = filter(lambda each: each in ["a", "e", "i", "o", "u"], data)
# print(list(result))
#
#
#
# # reduce()
#
# from functools import reduce
# data = [1,2,3,4,5]
#
# def multiply_all_elements(e1, e2):
#     return e1*e2
#
# result = reduce(multiply_all_elements, data)
# print(result)
#
#
#
#
# from functools import reduce
#
# result = reduce(lambda e1,e2: e1 * e2, data)
# print(result)
#
#
#
# # WAP a program to calculate the factorial of 7 using reduce() function with lambda
#
# from functools import reduce
#
# result = reduce(lambda e1,e2: e1*e2, range(1,8))
# print(result)
#
#
#
#
# def is_even(element):
#     return element%2 == 0
#
# result = is_even(3)
# print(result)
#
#
# result = lambda e:e%2==0
# print(result(3))
#
#
#
# def addition(a,b):
#     return a+b
#
# add = addition(2,3)
# print(add)
#
#
#
# def subtraction(a=3,b=1):
#     return a - b
#
# print(subtraction())
#
#
# def add(*args):
#     return sum(args)
#
# print(add(2,3))
# print(add(4,5,6,7))
#
#
# def subtract(**kwargs):
#     return kwargs["b"] - kwargs["a"]
#
# print(subtract(a = 2,b =3))
# print(subtract(a= 2,b= 3,c= 4,d= 5,e= 6))
#
#
# def calc(a,b,c,d,e,*args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#     print(args)
#     print(kwargs)
#
# calc(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, name = "John", age = 34)
#
#
#
# # 1. “Python+is+an+awesome+language”.
# # Split the given string to get a list and join to get another string “Python is an awesome language”
#
#
# a = "Python+is+an+awesome+language"
# b = a.split("+")
# print(b)
# c = " ".join(b)
# print(c)
#
#
#
# # 2. Write a Python program to create a dictionary from a string. Track the count of the
# # letters from the string.
# # Input = “broadway”
# # Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}
#
#
#
# a = "broadway"
# req_dic = {}
# for each in a:
#     req_dic.update({each:a.count(each)})
# print(req_dic)
#
#
#
# # 4. Write a program to check whether a string is anagram or not.
# # An anagram of a string is another string that contains the same characters,
# # only the order of characters can be different. For example, “silent” and “listen” are an anagram of each other.
#
#
#
# inp = input("Enter a string: ")
# inp2 = input("Enter another string: ")
# if sorted(inp.lower()) == sorted(inp2.lower()):
#     print("It is an anagram.")
# else:
#     print("It is not an anagram")
#
#
# # 5. Check whether a number is palindrome or not. Palindrome numbers are those which remain same even on reversing.
# # Examples – 111, 131, 222, 212 etc.
# # Input: 121 => The number is palindrome
# # Input: 321 => The number is not palindrome
#
#
#
# inp1 = input("Enter a number: ")
# if inp1 == inp1[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")
#
#
#
# # 6. WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours
# # up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# # Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# # You should use input to read a string and float() to convert the string to a number.
#
#
#
# hrs_worked = float(input("Enter number of hours worked: "))
# rate = float(input("Enter the rate per hour: "))
#
# if hrs_worked <= 40:
#     gross_pay = hrs_worked * rate
#     print(f"Your wage is ${gross_pay}")
# else:
#     gross_pay = (40 * rate) + ((hrs_worked - 40)* 1.5 * rate)
#     print(f"Your wage is ${gross_pay}")
#
#
#
# data = ["a", "e", "i", "o", "u"]
# print(list(enumerate(data)))
#
#
# for x,y in enumerate(data):
#     print(x,y)
#
#
# a = 1
# while a<10:
#     print(a)
#     a+=1
#
# a = 1
# while a<10:
#     print(a)
#     a+=1
#     if a == 4:
#         a+=1
#         continue
#
#
# a = 1
# while a<10:
#     print(a)
#     a+=1
#     if a==5:
#         break
# print("Found 5")
#
#
# WAP to delete all the occurrences of a specified character in a given string
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chracter in  given string”
#
#
# S = "All the occurrences of a specified character in a given string"
# a = ""
# rem_letter = input("Enter a letter: ")
# for each in S.lower():
#     if each == rem_letter.lower():
#         continue
#     a = a + each
# print(a)
#
#
# Create a new list of repeated items from a provided list:
# nums = [3, 4, 2, 2, 1, 3, 3, 3]
# Output = [3, 2]
#
#
# nums = [3,4,2,2,1,3,3,3]
# num1 = []
# for num in nums:
#     if nums.count(num)>1 and num not in num1:
#         num1.append(num)
# print(num1)
#
#
# data = [1,2,3,4,5]
# result = [each*3 for each in data]
# print(list(result))
#
#
# data = [1,2,3,4,5,6,7,8,9,10]
# result = [each for each in data if each % 2 == 0]
# print(list(result))
#
# result = [each for each in range(1,10,2)]
# print(result)
#
#
# result = {key: value for key, value in [("name", "Jason"), ("age", 30), ("address", "KTM")]}
# print(result)
#
#
# Operators in Python: Arithmetic, Logical, Relational/Comparison, Assignemnt, Membership and Identity
# Arguments in Python: Positional, Default/Key, Arbitrary
#
# Built-in-functins of Python are also known as higher-order-functions
# map(function, iterable), filter(function, iterable), reduce(function, iterable)
# For using reduce(), we need to "From functools import reduce"
# If there is only one task for a function, we use lambda
#
#
#
#
# list() has the following methods: a.append("a"), a.extend(["b", "c", "d"]), a.insert(0,"A"), a.remove("a"), a.pop(), a.clear(), a.count("a"), a[0]
# tuple() has the following methods: a.count("a"), a[1]
# set() has the following methods: a.add("a"), a.update(["a", "b", "c","d")], a.remove("a"), a.discard("a"), a.clear(), a.pop("a"), a.difference(b), a.union(b),
# a.intersection(b), a.symmetric_difference(b), a.update_symmetric_difference(b), a.is_disjoint(b), a.issubset(b), a.is_superset(b)
#
# Slicing and concatenation can also be done
# a+b is concatenation and a[:2] is slicing

# def decorator(func):
#     def wrapper():
#         print("Transaction started...")
#         func()
#         print("Transaction ended.....")
#     return wrapper
#
#
# def hello():
#     print("Execution of steps......")
#     print("Step1")
#     print("Step2...")
#     print("Final step")
#
#
# hello1 = decorator(hello)
# hello1()

# def creator1():
#     i = 1
#     while i<201:
#         yield i
#         i+=1
#
# x = creator1()
# print(next(x))
# print(next(x))
# print(next(x))
# print(list(x))


# def creater():
#     i = 1
#     while i<201:
#         yield i
#         i+=1
#
# x = creater()
# print(next(x))
# print(next(x))
# print(next(x))
# print(list(x))
#
#
# def decorator(func):
#     def wrapper():
#         print("Transaction started.....")
#         func()
#         print("Transaction ended........")
#     return wrapper
#
#
# def hello():
#     print("Transaction processing")
#     print("Step 1 completed")
#     print("Step 2 completed")
#
# hello1 = decorator(hello)
# hello1()
#
#
#
# data = [1,2,3,4,5,6]
# result = map(lambda e:e*3, data)
# print(list(result))
#
#
# data = ["a", "b", "c", "d", "e", "f"]
# result = filter(lambda e: e in ["a", "e", "i", "o", "u"], data)
# print(list(result))
#
#
#
# from functools import reduce
#
# data = [1,2,3,4,5]
# result = reduce(lambda e1,e2: e1*e2, data)
# print(result)
#
#
# result = reduce(lambda e1, e2:e1*e2, range(1,6))
# print(result)

