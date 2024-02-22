#
# def decorator(func):
#     def inner_function(*args, **kwargs):
#         print("The addition of the numbers is given below")
#         return func(*args, **kwargs)
#     print("Thank you")
#     return inner_function
#
#
#
#
# @decorator
# def addition(a,b):
#     return a + b
# print(addition(2,3))
#
#
#
# # WAP to create a decorator function which calculates the total time to execute the following functions
#
#
# def time_(func):
#     def inner_function(*args, **kwargs):
#         import time
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"The total time elapsed was {end - start}.")
#         return result
#     return inner_function
#
#
# @time_
# def time_taken():
#     for i in range(100000000):
#         continue
#     else:
#         print("Loop complete")
#
# time_taken()
#
#
# # Create a decorator function which changes the lower case input in a function to upper case
#
#
# def turn_to_upper_case(func):
#     def inner_func(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return inner_func
#
#
#
# @turn_to_upper_case
# def message(msg):
#     return msg
#
#
# m1 = message("Hi, this is turning lower case to upper case.")
# print(m1)
#
#
#
# def login_required(func):
#     def inner_func(*args, **kwargs):
#         Password = input("Enter password: ")
#         if Password == "1234":
#             return func(*args, **kwargs)
#         else:
#             return "Incorrect password"
#     return inner_func
#
#
#
# @login_required
# def addition(a, b):
#     return a + b
# print(addition(2, 3))


# class Vehicle:
#     engine_type = "Petrol"
#
#     def __init__(self, color, no_of_seats):
#         self.color = color
#         self.no_of_seats = no_of_seats
#
#     def get_details(self):
#         return f"The color of the vehicle is {self.color} and the number of seats it has is {self.no_of_seats}."
#
#
#
#
# v1 = Vehicle("Green", 4)
# v2 = Vehicle("Red", 6)
#
# print(v1.color)
# print(Vehicle.engine_type)
#
# print(v1.get_details())
# print(Vehicle.get_details(v2))



# class A:
#     a = 1
#
# class B(A):
#     b = 2
#
# class C(B):
#     c = 3
#
# class D(C):
#     d = 4
#
# ob1 = D()
# print(ob1.a)
# print(D.mro())


# Create a class Person with instance attributes name and age.
# Create a method get_details in this class to print name and age.


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_details(self):
#         return f"The name is {self.name} and age is {self.age}."
#
# p1 = Person("Jon", 21)
#
# print(p1.get_details())



# Object oriented Programming is a programming paradigm which breaks down problems into classes and objects
# Inheritance, Encapsulation, Polymorphism, Abstraction
# Inheritance is the process of accessing the parent class from the child classes
# Single, Multiple, Multilevel, Hierarchical, Hybrid: Types of Inheritance


# Encapsulation is the process of hiding the class attributes so that it can be only accessed within the class
# Public, Protected and Private


# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address
#     def get_details(self):
#         return f"The name is {self.name} and age is {self._age}. The address is {self.__address}."
#
#     def __get_name_and_age(self):
#         return f"The name is {self.name} and age is {self._age}."
#
# p1 = Person("Jon", 21, "KTM")
#
#
#
# print(p1._age)
# print(p1.get_details())
# print(Person.get_details(p1))



# Polymorphism means many forms of same funtion
# Method/Function Overloading
# Operator Overloading


# Python does not support mehtod/fucntion overloading. It takes the latest defined function if under same names

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def get_details(self):
#         return f"Name is {self.name} and age is {self.age}"
#
#     def get_details(self):
#         return f"Name is {self.name} and age is {self.age} and address is {self.address}"
#
#
#
# p1 = Person("Jon", 25, "KTM")
# print(p1.get_details())






# Operator overloading

# a = 1
# b = 2
# c = a + b
# print(c)
#
# c = a.__add__(b)
# print(c)


# Create another class Employee with attributes salary and designation and inherits
# the Person class. Create a method get_details in this class to print name, age, salary and designation of
# the Employee.



# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address
#     def get_details(self):
#         return f"The name is {self.name} and age is {self._age}. The address is {self.__address}."
#
#     def __get_name_and_age(self):
#         return f"The name is {self.name} and age is {self._age}."
#
# class Employee(Person):
#     def __init__(self, name, age, address, salary, designation):
#         super().__init__(name, age, address)
#         self.salary = salary
#         self.designation = designation
#
#     def get_details(self):
#         print(super().get_details())
#         return f"The salary is {self.salary} and designation is {self.designation}."
#
# e1 = Employee("Jon", 22, "KTM", 80000, "IT Manager")
# print(e1.get_details())


# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
# Add the radius of the circles and print the result.
# Do the above task using a method and then a magic method.
# Compare the size of the circle and print the result using magic method.


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def sum_of_circle(self, other):
#         return self.radius + other.radius
#
#     def __add__(self, other):
#         return self.radius + other.radius
#
#
# c1 = Circle(5)
# c2 = Circle(4)
#
# print(c1.sum_of_circle(c2))
#
# print(c1+c2)


# Create a class Department with parameters name and number_of_students.
# Create a method total students, which takes department object as a parameter and
# return the total number of students from all departments.


# class Department:
#     def __init__(self, name, number_of_students):
#         self.name = name
#         self.number_of_students = number_of_students
#
#     def total_students(self, *others):
#         result =  [each.number_of_students for each in others]
#         return sum(result) + self.number_of_students
# d1 = Department("IT", 14)
# d2 = Department("cs", 10)
# d3 = Department("Python", 5)
#
# print(d1.total_students(d2, d3))



class Vehicle:
    __engine_type = "Petrol"

    @classmethod
    def change_engine_type(cls, new_engine_type):
        cls.__engine_type = new_engine_type

    @classmethod
    def get_engine_type(cls):
        return cls.__engine_type

    @staticmethod
    def get_info():
        return "These cars are awesome."

v1 = Vehicle()
print(Vehicle.get_engine_type())
Vehicle.change_engine_type("Disel")
print(Vehicle.get_engine_type())
print(Vehicle.get_info())

