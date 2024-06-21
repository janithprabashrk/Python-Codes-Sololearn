class MyClass:
    def __init__(self):
        self.__private_attribute = 'I am private!'

# Outside the class
obj = MyClass()

# Accessing the private attribute using name mangling
print(obj._MyClass__private_attribute)  # Output: I am private!
