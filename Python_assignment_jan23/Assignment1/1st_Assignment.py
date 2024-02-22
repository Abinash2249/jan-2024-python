# 1. “Python+is+an+awesome+language”.
# Split the given string to get a list and join to get another string “Python is an awesome language”

data = "Python+is+an+awesome+language"
result = data.split("+")
print(result)

result2 = " ".join(result)
print(result2)












# 2. Write a Python program to create a dictionary from a string. Track the count of the
# letters from the string.
# Input = “broadway”
# Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}

word = "broadway"
dic = {}
for each in word:
    dic.update({each: word.count(each)})
print(dic)













# 3. Write a Python program to combine two dictionaries by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

all_keys = list(set(d1.keys()).union(set(d2.keys())))
print(all_keys)
result = dict()

for key in all_keys:
    if key in d1 and key in d2:
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d1.get(key) or d2.get(key)

print(result)


# d1_a = d1.get("a")
# d1_b = d1.get("b")
# d1_c = d1.get("c")
# d2_a = d2.get("a")
# d2_b = d2.get("b")
# d2_d = d2.get("d")
#
# d3_a = d1_a + d2_a
# d3_b = d1_b + d2_b
# d3_c = d1_c
# d3_d = d2_d
#
# output = {'a': d3_a, 'b': d3_b, 'c': d3_c, 'd': d3_d}
# print(output)












# 4. Write a program to check whether a string is anagram or not.
# An anagram of a string is another string that contains the same characters,
# only the order of characters can be different. For example, “silent” and “listen” are an anagram of each other.

first_word = input("Enter a word: ")
second_word = input("Enter another word: ")
if sorted(first_word) == sorted(second_word):
    print("It is an anagram.")
else:
    print("It is not an anagram.")








# 5. Check whether a number is palindrome or not. Palindrome numbers are those which remain same even on reversing.
# Examples – 111, 131, 222, 212 etc.
# Input: 121 => The number is palindrome
# Input: 321 => The number is not palindrome

num1 = str(input("Enter a number: "))
if num1 == num1[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")









# 6. WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours
# up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.


hours = float(input("Enter the number of hours: "))
rate = float(input("Enter the rate per hour: "))
if hours <= 40:
    gross_pay = hours * rate
    print(f"Your wage is {gross_pay}")
else:
    gross_pay = 40 * rate
    ov_time = (hours - 40) * 1.5 * rate
    new_gross_pay = gross_pay + ov_time
    print(f"Your wage is {new_gross_pay}")