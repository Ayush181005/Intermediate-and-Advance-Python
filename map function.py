# Map Function
# map(function_to_apply, list_of_iterables)

h1 = [1, 2, 4, 5, 7]

# 1st Way:-
sq = []
for i in h1:
    sq.append(i**2)
print(sq)

# Another Way:-
def square(n):
    return n**2
# sq = map(square, h1)    # This becomes a map object so we will type cast it into a list
sq = list(map(square, h1))
print(sq)

