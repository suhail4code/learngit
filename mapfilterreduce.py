######### map function is here ###########

# def cube(x):
#     return x*x*x

# l=[1,2,3,4,6,74,2,4]

# newlist =  map(cube, l)
# print(type(newlist))
# newlist= list(map(cube, l))
# print(newlist)


########## filter############
# def filter_function(a):
#     return a>4

# l=[1,2,3,4,6,74,2,4,5,6,7,8,9,10]
# newlist = filter(filter_function,l)

# print(newlist)
# newlist = list(filter(filter_function,l))
# print(newlist)
from functools import reduce 

number = [23,34,45,56,54,43]

def sum(x,y):
    return x+y

sum = reduce(sum, number)

print(sum)


