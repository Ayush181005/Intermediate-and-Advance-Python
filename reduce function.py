from functools import reduce

def sum_num(a, b):
    return a+b

li1 = reduce(sum_num, [1, 2, 3, 4])
# First it takes 1 and 2
# Then, (1+2) and 3 that is 3 and 3
# Then, (3+3) and 4 that is 6 and 4
# That prints 10
print(li1)