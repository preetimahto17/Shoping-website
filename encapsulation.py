class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.year = year  # Public attribute
    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_make())  # Accessing private attribute
print(my_car.year)  # Accessing public attribute
