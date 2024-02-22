class Vehicle:
    __engine_type = "Petrol"  # class attribute

    @classmethod
    def change_engine_type(cls, new_engine_type):
        cls.__engine_type = new_engine_type


    @classmethod
    def get_engine_type(cls):
        return cls.__engine_type

    @staticmethod
    def get_info():
        return "These cars are awesome"


v1 = Vehicle()
# print(v1.engine_type) # Petrol
# v1.engine_type = "diesel"
# print(v1.engine_type)  # diesel

print(Vehicle.get_engine_type())
Vehicle.change_engine_type("Diesel")
print(Vehicle.get_engine_type())


print(Vehicle.get_info())  # These cars are awesome