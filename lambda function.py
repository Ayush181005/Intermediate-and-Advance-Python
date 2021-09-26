# Syntax - lambda argument : manipulate the argument, it is a single line function

# def add(a, b):
#     return a+b
# print(add(4, 6))

add = lambda x,y : x+y
print(add(4, 6))

add = lambda x,y:x>y
print(add(4, 6))

a = [(1, 2), (4, 5), (555, 34)]
a.sort(key=lambda x:x[1])
print(a)
