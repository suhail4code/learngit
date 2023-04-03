# a = input("Enter the number: ")

# print(f"Multiplication table of {a} is ")
# try:
#    for i in range(1,11):
#       print(f"{int(a)} X {i}= {int(a)*i}")
# except:
#     print("These are some importent lines that have to executed")
#     print("sorry some error occured here")


# try:
#  l = [1,2,3,4,53,2]
#  i = int(input("Enter the index: "))
#  print(l[i])

# except:
#     print("some error occured ")

# finally:
#     print("im always executed here")

a = int(input("Enter the value bt 4 to 10"))

if(a<5 or a> 9):
    raise VlaueError("Valse should be between 5 and 9")

