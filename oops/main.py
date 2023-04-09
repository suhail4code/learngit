class person :
    name= "suhail"
    occupation = "student"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "himanshu"

b= person()
b.name= "aman"
b.occupation="flutter"
print(a.name)
a.info()
b.info()
c= person()
print(c.name)
c.info()