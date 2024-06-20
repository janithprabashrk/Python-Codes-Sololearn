def greet():
    return "Welcome"

#takes a function as an argument

def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        mod_message = orig_message.upper()
        return mod_message
    return wrapper

greet_upper = uppercase(great)
print(greet_upper())