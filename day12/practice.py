# Arithmetic operators: +, -, *, /, %, **
# Logical operators: and, or
# Relational or Comparison operators: ==, <=, >=, <, >
# Assignment operators: =+, -+, *=, /+
# Membership operators: in, not in
# Identity operators: is, is not


# Data types in Python
# Mutable datatypes: list(), dict(), set()
# Immutable datatypes: tuple(), str(), numbers
# Boolean datatypes: True, False


# Boolean datatypes are used in assignment operators, relational operators, logical operators, membership operators and identity operators


# List methods: .append(), .extend(), .insert, .pop(), .clear(), .remove(), .index(), .count(), .copy(), .sort(), .reverse()

a_list = [1,2,3,4,5,6,7]
print(a_list[3])
print(a_list[2:4])
print(a_list[-1])
empty_list = []
print(empty_list)

a_list.append(8)
print(a_list)

a_list.extend([9,10,11])
print(a_list)

a_list.insert(0,0)
print(a_list)

item_popped_in_a_list = a_list.pop()
print(a_list)
print(item_popped_in_a_list)

a_list.remove(0)
print(a_list)

a_list.clear()
print(a_list)



# Dictionary methods: .update, .get(), .values(), .keys(), .items()

a_dict = {"name": "Abinash", "age": 22, "address": "Pepsicola"}
name_dict = a_dict.get("name")
print(name_dict)
age_dict = a_dict["age"]
print(age_dict)
a_dict.update({"height": "5ft 7", "gender": "male"})
print(a_dict)
a_dict.update(language = "Python")
print(a_dict)
a_values_dict = a_dict.values()
a_keys_dict = a_dict.keys()
a_items_dict = a_dict.items()
print(list(a_values_dict))
print(list(a_keys_dict))
print(list(a_items_dict))



# Tuple methods: .count(), .index()

a_tuple = (1,2,1,2,1,1,1)
print(a_tuple)

print(a_tuple.count(1))

print(a_tuple.index(1,3,5))


# Set mehthods: .update(), .remove(), .clear(), .pop(), .add(), .intersection(), .union(), .difference(), .isdisjoint(), .issubset(), .issuperset(), .symmetric_difference(), .symmetric_difference_update

a_set = {"a", "e", "i", "o", "u"}
a_set.add(1)
print(a_set)
a_set.update({1,2,3,4,5})
print(a_set)
a_set.remove(2)
print(a_set)
popped = a_set.pop()
print(a_set)
print(popped)

# String methods: "".join, .split(), .index(), .count(), .capitalise(), .upper(), .lower(), .title()

a = ["Python", "is", "an", "awesome", "language"]
b = " ".join(a)
print(b)
d = "Python is an awesome langugae"
e = d.split(" ")
print(e)

print(d.title())
print(d.capitalize())
print(d.upper())
print(d.lower())

# Looping in Python
# for loop is used for iterables

for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)

for each in ["a", "e", "i", "o", "u"]:
    print(each)



# while loop is used for conditions

a = 1
while a < 10:
    print(a)
    a += 1


# Conditions in Python
# if, if...else, if.....elif, if.....elif....else
# ternary if

a = 10
if a % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")




# enumerate() counts the items or elements from a specific point

a = ["a", "e", "i", "o", "u"]
b = enumerate(a)
print(list(b))


for i,j in enumerate(a, start = 1):
    print(i,j)



# built-in-functions
# max(), min(), sum(), len(), print(), input(), any(), all(), sorted(), reversed()

print(max(12,11,14,2))
print(all([True, 1, "apple"]))

# break, continue, pass

for each in [1,2,3,4,5]:
    print(each)
    if each == 4:
        break


for each in [1,2,3,4,5]:
    if each==3:
        continue
    print(each)

a = 1
while a<10:
    if a == 3:
        a+=1
        continue
    print(a)
    a+=1


data = [1,2,3,4,5,6,7,8,9]
result = []
for each in data:
    if a%2 == 0:
        result.append(each)
print(result)

result = [each*3 for each in data if each%2 == 0]
print(result)






