class employee:
    def __init__(self ,name,id):
        self.name = name
        self.id=id

    def showdetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(employee):
    def showlang(self):
        print("the default language is python")

e1 = employee("himanshu", 1)

e1.showdetails()
e2=programmer("aman", 7)
e2.showdetails()
e2.showlang()

