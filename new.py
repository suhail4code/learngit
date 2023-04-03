print("this is the new file for understanding the git tutorial")

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)



a=int(input("Enter the number to find the factorial of any number"))

print(factorial(a))