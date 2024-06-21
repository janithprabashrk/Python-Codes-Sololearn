class MyClass:
    def __init__(self):
        self.__private_attribute = 'I am private!'

    def get_private_attribute(self):
        return self.__private_attribute

# Outside the class
obj = MyClass()

# Attempting to access the private attribute directly from outside the class
# This will result in an AttributeError due to name mangling
try:
    print(obj.__private_attribute)
except AttributeError as e:
    print(e)  # Output: 'MyClass' object has no attribute '__private_attribute'

# Accessing the private attribute using a getter method (recommended)
print(obj.get_private_attribute())  # Output: I am private!

# The next level of data hiding involves making an attribute private. 
# This is achieved by prefixing the attribute name with two underscores (e.g., __attribute). 
# In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation.
# This method is used for sensitive or internal data, strongly discouraging external access.
# Accessing a private attribute with double underscores from outside the class causes an error, but it's accessible within class methods.