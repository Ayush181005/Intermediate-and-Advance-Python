# List Comprehension:-
list_1 = [1, 32, 4, 5, 45, 4, 4, 3, 3, 3, 5, 6, 3, 343, 343, 5, 4]

divisible_by_3 = []
for item in list_1:
    if item % 3 == 0:
        divisible_by_3.append(item)
print('Without using List Comprehensions, the list of divisible_by_3 nos. is:-\n', divisible_by_3 ,"\t(in 5 lines of code)")

print("With Using List Comprehensions, the list of divisible_by_3 nos. is:-\n", [item for item in list_1 if item%3==0], "\t(in 1 line of code)")

# Dictionary Comprehension
dict1 = {'a':45, 'b':65, 'A':5} # - Adding all lower and uppercase elements to one
print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

# Set Comprehension
squared = {x**2 for x in [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5]}     # It will take every repeating number once only because after coming in the set, each value is shown only once in a set
print(squared)

# Generator Comprehension
# gen = (i for i in range(56))    # Generator object will get created
gen = (i for i in range(56) if i%3==0)    # It can also be like this
print(gen)
for item in gen:
    print(item)