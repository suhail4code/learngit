x= 4
print(x)

def hello():
    global x
    x=10
    print(f"local variable {x}")

hello()
print(x)