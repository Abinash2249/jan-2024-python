# WAP a program to calculate the factorial of 7 using reduce() function with lambda

from functools import reduce

result = reduce(lambda el1, el2: el1 * el2,range(1,8))
print(result)   # 5040


