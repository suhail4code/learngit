def welcome():
    print("you are welcome my friend from suhail")


print(__name__)

# the code bottom from the __name__=="__main__  is run only when the file directly executed "
# if this file is imported in any other file then the code after the next line will not be executed

if __name__ == "__main__":
    welcome()