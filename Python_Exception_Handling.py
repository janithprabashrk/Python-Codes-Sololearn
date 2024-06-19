balance = -50
try:
    if balance < 0:
        raise ValueError("Wrong value")
except ValueError:
    print("Value ERROR")
