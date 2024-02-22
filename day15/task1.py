# Create a class Person with instance attributes name and age.
# Create a method get_details in this class to print name and age.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name of the student is {self.name} who is of age {self.age}."

p1 = Person("Jon", 21)
p2 = Person("Marry", 22)


print(p1.name)
print(p1.get_details())
print(p2.get_details())