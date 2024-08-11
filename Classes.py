class puppy():
    def __init__(self, name, favourite_toy): #__init__ job is to assogn values to any variables
        self.name = name       #Self is how you represent to the current instance of the class
        self.favourite_toy = favourite_toy

    def play(self):
        print(self.name + " is playning with the " + self.favourite_toy)


Rex = puppy("Rex", "Ball") #create object

Rex.play() #call the method