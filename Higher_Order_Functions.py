def welcome(name):
    return "Welcome " + name

def bye(name):
    return "Plyn " + name + " Hutto Yanna"

def processUser(func, name): #higher order Function
    return func(name)

def main():
    print("Select one of them:")
    print("1. Bye")
    print("2. Welcome")
    n = int(input())
    print("Enter a name:")
    name = input()
    if n == 1 :
        print(processUser(bye, name))
    else:
        print(processUser(welcome, name))

if __name__ == "__main__":
    main()

"""In Python, functions that operate with other functions — that is, take another function as an argument or return a function -  are called Higher-Order Functions. They are particularly useful for processing various functions and returning specific results."""