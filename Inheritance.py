# Define a base class 'animal'
class Animal:
    # Initialize with a name
    def __init__(self, name):
        self.name = name

    # Define a method 'move' that prints "moving"
    def move(self):
        print("moving")

# Define a subclass 'Dog' that inherits from 'animal'
class Dog(Animal):
    # Define a method 'bark' that prints "Woooof!"
    def bark(self):
        print("Woooof!")

# Create an instance of 'Dog' with the name "Rexy"
my_dog = Dog("Rexy")

# Print the name of the dog
print(my_dog.name)

# Call the 'bark' method to make the dog bark
my_dog.bark()  # Commented out to suppress the bark output
