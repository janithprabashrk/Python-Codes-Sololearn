cars = ["Lamborgini", "Benz", "Chavrolete", "Landrover", "Toyota"]

def upperClass(cars):
    return cars.upper()

Uppered = map(upperClass, cars)

Uppered = list(Uppered)

print(Uppered)

"""The map() function applies a specified function to every element in an iterable, like lists or tuples. 
It produces a result that can be transformed into a list using the list() function for easy viewing or further use."""