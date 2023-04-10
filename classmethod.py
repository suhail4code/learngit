# class employee:

#     company = "Apple"
#     def show(self):
#         print(f"the name is {self.name} and company is {self.company}")


#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
    
# e1 = employee()
# e1.name = "suhail"
# e1.show()

# e1.changeCompany("tesla")
# e1.show()

# print(employee.company)



class employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e = employee("suhail", 12000)
print(e.name)
print(e.salary)


string = "suhail-12000"
e2 = employee.fromstr(string)
print(e2.name)

print(e2.salary)