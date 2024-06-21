# Define the base class 'Vehicle'
class Vehicle:
    # Initialize with make, model, and odometer
    def __init__(self, make, model, odometer=0):
        self.make = make
        self.model = model
        self._odometer = odometer  # 'Protected' attribute

    # Method to be overridden
    def description(self):
        print(f"Vehicle make: {self.make}, model: {self.model}")
        print(f"Odometer reading: {self._odometer} km")

# Define a subclass 'Car' that inherits from 'Vehicle'
class Car(Vehicle):
    # Initialize with make, model, and odometer
    def __init__(self, make, model, odometer=0):
        super().__init__(make, model, odometer)

    # Override the description method and call the parent's description method
    def description(self):
        super().description()
        print("This is a car.")

# Create an instance of 'Car'
car = Car("Toyota", "Corolla", 5000)

# Call the description method on the instance
car.description()  # Output: Vehicle make: Toyota, model: Corolla
                   #         Odometer reading: 5000 km
                   #         This is a car.
