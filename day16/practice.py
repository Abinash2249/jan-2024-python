class Vehicle:  # class
    engine_type = "petrol"  # class attribute => class property

    def __init__(self, color, number_of_seats):     # Constuctor        # self means object
        self.color = color      # instance attribute => instance property
        self.number_of_seats = number_of_seats      # instance attribute => instance property
    def get_info(self):     # instance method
        print(f"The color of car is {self.color} and the number of seats available are {self.number_of_seats}.")

    def set_color(self, new_color):     # instance attribute => instance method
        self.color = new_color

v1 = Vehicle("green", 4)    # object
v2 = Vehicle("yellow", 6)   # object

print(v1.color)
print(v2.color)

print(v1.number_of_seats)
print(v2.number_of_seats)


v1.set_color("orange")
print(v1.color)


