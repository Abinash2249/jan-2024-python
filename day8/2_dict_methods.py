# update(), pop(), get(), keys(), values(), items(), clear()

# update()
student = {"name": "Hary", "age": 30, "address": "KTM"}
print(student)

student.update({"roll": 12, "email": "h@email.com"})
print(student)  # {'name': 'Hary', 'age': 30, 'address': 'KTM', 'roll': 12, 'email': 'h@email.com'}

student.update(height="5.7", phone=989898098)
print(student)


# pop()
student = {"name": "Hary", "age": 30, "address": "KTM"}
age = student.pop("age")
print(student)  # {'name': 'Hary', 'address': 'KTM'}
print(age)  # 30

# get()
student = {"name": "Hary", "age": 30, "address": "KTM"}
address = student.get("address")
print(address)

roll = student.get("roll")
print(roll)     # None

roll = student.get("roll", 10)
print(roll)

address = student.get("address", "PKR")
print(address)  # KTM


# keys()
student = {"name": "Hary", "age": 30, "address": "KTM"}
print(student.keys())   # dict_keys(['name', 'age', 'address'])
keys = list(student.keys())
print(keys)     # ['name', 'age', 'address']


# values
student = {"name": "Hary", "age": 30, "address": "KTM"}
print(student.values())     # dict_values(['Hary', 30, 'KTM'])

values = list(student.values())
print(values)   # ['Hary', 30, 'KTM']


# items()
student = {"name": "Hary", "age": 30, "address": "KTM"}
print(student.items())  # dict_items([('name', 'Hary'), ('age', 30), ('address', 'KTM')])

items = list(student.items())
print(items)    # [('name', 'Hary'), ('age', 30), ('address', 'KTM')]


# clear()
student = {"name": "Hary", "age": 30, "address": "KTM"}
student.clear()
print(student)  # {}


# Membership operation in dictionary
student = {"name": "Hary", "age": 30, "address": "KTM"}
print("name" in student)    # True
print("Harry" in student)    # False





