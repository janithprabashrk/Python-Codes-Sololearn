def welcome(name):
  return "Welcome, " + name
greet = welcome

print(greet("Janith"))


"""After assigning a function to a variable, you can use the variable to call the function.Call the welcome() function using the variable it's assigned to """

def shout(text):  
    return text.upper()
yell = shout
print(yell("Hello"))