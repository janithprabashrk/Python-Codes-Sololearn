class Car:
    def __init__(self, make, model, year, color):
        # Initialize the attributes of the Car class
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_running = False

    def display_info(self):
        # Method to display information about the car
        print(f"{self.year} {self.make} {self.model} in {self.color}")

    def start_engine(self):
        # Method to simulate starting the car's engine
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        # Method to simulate stopping the car's engine
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already off.")

    def paint(self, new_color):
        # Method to change the color of the car
        old_color = self.color
        self.color = new_color
        print(f"The {self.make} {self.model} has been repainted from {old_color} to {new_color}.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020, "Red")

# Display the car's information
my_car.display_info()

# Start the car's engine
my_car.start_engine()

# Try starting the engine again
my_car.start_engine()

# Stop the car's engine
my_car.stop_engine()

# Try stopping the engine again
my_car.stop_engine()

# Change the car's color
my_car.paint("Blue")

# Display the car's information again to see the new color
my_car.display_info()
