class Pet(object):
    """this is a pet class"""  # pet.__doc__

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        print("{} is a {}".format(self.name, self.species))


class Dog(Pet):
    """this is a dog class"""

    def __init__(self, name, color):
        Pet.__init__(self, name, "Dog")
        self.color = color

    @property
    def getColor(self):
        return self.color


jerry = Pet("jerry", "mouse")

Pet.__str__(jerry)

billy = Dog("billy","black")

print(billy.getSpecies())
billy.__str__()

print(billy.getColor)