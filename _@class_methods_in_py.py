class MyClass:
    class_variable = 0
    
    @classmethod
    def class_method(cls, value):
        cls.class_variable += value
        return cls.class_variable

# Calling the class method directly using the class name
result = MyClass.class_method(5)
print(result)  # Output will be 5

result = MyClass.class_method(3)
print(result)  # Output will be 8

#To call a class method you don't need to create an instance of the class. 
# Instead, just use the class name, followed by a dot and the class method name.

