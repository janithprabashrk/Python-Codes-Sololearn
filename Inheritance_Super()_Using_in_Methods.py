# Define the base class 'Vehicle'
class Vehicle:
    # Initialize with make and model
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Method to be overridden
    def description(self):
        print(f"Vehicle make: {self.make}, model: {self.model}")

# Define a subclass 'Car' that inherits from 'Vehicle'
class Car(Vehicle):
    # Initialize with make, model, and number of doors
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    # Override the description method and call the parent's description method
    def description(self):
        super().description()
        print(f"This car has {self.doors} doors.")

# Define a subclass 'Motorcycle' that inherits from 'Vehicle'
class Motorcycle(Vehicle):
    # Initialize with make, model, and type
    def __init__(self, make, model, motorcycle_type):
        super().__init__(make, model)
        self.motorcycle_type = motorcycle_type

    # Override the description method and call the parent's description method
    def description(self):
        super().description()
        print(f"This motorcycle is a {self.motorcycle_type} type.")

# Create instances of 'Car' and 'Motorcycle'
car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", "cruiser")

# Call the description method on each instance
car.description()  # Output: Vehicle make: Toyota, model: Corolla
                   #         This car has 4 doors.
motorcycle.description()  # Output: Vehicle make: Harley-Davidson, model: Sportster
                          #         This motorcycle is a cruiser type.
