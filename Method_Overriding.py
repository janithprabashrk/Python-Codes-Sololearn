# Define the base class 'Animal'
class Animal:
    # Method to be overridden
    def sound(self):
        print("Some generic animal sound")

# Define a subclass 'Dog' that inherits from 'Animal'
class Dog(Animal):
    # Override the sound method
    def sound(self):
        print("Woof Woof!")

# Define a subclass 'Cat' that inherits from 'Animal'
class Cat(Animal):
    # Override the sound method
    def sound(self):
        print("Meow Meow!")

# Create instances of 'Dog' and 'Cat'
dog = Dog()
cat = Cat()

# Call the sound method on each instance
dog.sound()  # Output: Woof Woof!
cat.sound()  # Output: Meow
