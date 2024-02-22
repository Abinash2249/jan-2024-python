# Create a class Person with instance attributes name and age.
# Create a method get_details in this class to print name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"The name of the person is {self.name} and age is {self.age}."

p1 = Person("Jon", 21)
p2 = Person("Mary", 22)



# Create another class Employee with attributes salary and designation and inherits
# the Person class. Create a method get_details in this class to print name, age, salary and designation of
# the Employee.


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"Their salary is {self.salary} and designation is {self.designation}."

e1 = Employee("Jon", 21, 21000, "Manager")

print(e1.get_details())


