# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function that returns True for even numbers
def is_even(number):
    return number % 2 == 0

# Using filter() to get only even numbers from the list
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list
even_numbers = list(even_numbers)

print(even_numbers)

""""Translate course
The filter() function, just like the map() function, 
takes in a function and an iterable as arguments.
The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable and return only those for which the function evaluates to True."""