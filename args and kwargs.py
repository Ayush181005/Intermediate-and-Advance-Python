# *args and **kwargs - It can be any name, just star is neccassary

# Normal method of calling function:-
'''
def function_1(name, age, roll_no):
    print("\nName:", name, "\nAge:", age, "\nRoll no.:", roll_no)

function_1("Ayush", 15, 6)
'''

# for *args:-
def function_1(*args):
    # print("The type of *args is:", type(args))        # args is a tuple

    if len(args) == 3:
        print("\nName:", args[0], "\nAge:", args[1], "\nRoll no.:", args[2])

    else:
        print("\nName:", args[0], "\nAge:", args[1])

function_1("Ayush", 15, 6)
function_1("Ayush", 15)

lis = ["Ayush", 15]
function_1(*lis)

# for **kwargs:-
def printMarks(**kwargs):
    # print("\n\nThe type of **kwargs is", type(kwargs), "\n")     # The type of **kwargs is dictionary

    for key, value in kwargs.items():
        print(key,":", value)

markDictionary = {"Ayush": 98, "Jaimit": 97, "Maanit": 99, "Hahaha": 80, "Dhairya": 100, "Heehee": 75, "Poorururu": 70}

printMarks(**markDictionary)

# for normal argument, *args, and **kwargs in the same function:-
def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key,":", value)

print("\n")
master("normal argument - string", *lis, **markDictionary)
