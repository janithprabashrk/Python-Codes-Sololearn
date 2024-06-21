class MyClass:
    def __init__(self):
        self._protected_attribute = 'I am protected!'

    def get_protected_attribute(self):
        return self._protected_attribute

# Outside the class
obj = MyClass()

# Accessing the protected attribute directly (not recommended)
print(obj._protected_attribute)  # Output: I am protected!

# Accessing the protected attribute using a getter method (recommended)
print(obj.get_protected_attribute())  # Output: I am protected!
