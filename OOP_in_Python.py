class Car:
    def __init__(self, make, model, year, color):
        # Initialize the attributes of the Car class
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        # Method to display information about the car
        print(f"{self.year} {self.make} {self.model} in {self.color}")

    def start_engine(self):
        # Method to simulate starting the car's engine
        print(f"The {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        # Method to simulate stopping the car's engine
        print(f"The {self.make} {self.model}'s engine has stopped.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020, "Red")


print(my_car.color)

# Display the car's information
my_car.display_info()

# Start the car's engine
my_car.start_engine()

# Stop the car's engine
my_car.stop_engine()

#To add attributes to a class, you must define the __init__ method. 
# This method's first parameter is always self, which represents the instance of the class. 
# Following self, you specify the attributes you wish to include. Then, inside the function, 
# you assign values to the initialized object's attributes, setting their initial state.

