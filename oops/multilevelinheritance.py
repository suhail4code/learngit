class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def showdetails(self):
        print(f"Name : {self.name}")
        print(f"species: {self.species}")

    
class Dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name,species="Dog")
        self. breed = breed
    def showdetails(self):
        animal.showdetails(self)
        print(f"breed : {self.breed}")


class goldenretriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "goldenretriever")
        self.color = color

    def showdetails(self):
        Dog.showdetails(self)
        print(f"color: {self.color}")




o = goldenretriever("tommy", "black",)
o.showdetails()