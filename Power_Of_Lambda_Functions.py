def mult(n):
    return lambda x: x * n

# Example usage:
doubler = mult(2) #n = 2 Then doubler = lambda x: x * 2
tripler = mult(3) #n = 3

print(doubler(5))  # Output: 10 Then Assigning Values for x = 5
print(tripler(4))  # Output: 12
