class person :
    def __init__(self,n,o):
        print("hey suhail")
        self.name = n
        self.occupation=o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("suhail","student")
b=person("srishti", "bekar ladki")

a.info()
b.info()



