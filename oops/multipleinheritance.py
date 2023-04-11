class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The name is {self.dance}")


class danceremployee(employee, dancer):
    def __init__(self, dance,name):
        self.name= name
        self.dance = dance


o = danceremployee("kathak", "shivani")
print(o.name)
print(o.dance)
o.show()