'''
Iterable - Object that can give us an iterator and has __getItem method
Iterator - Object where the next method is defined
Iteration - Iterating anything and fetching its next elements is known as iteration

Generators - These are iterators which can be iterated only once
'''
# for i in range(10000000):   # This will take a lot of RAM and also take time
#     print(i)

    # A Generator is something which is not printing such things but it is capable of generating these numbers

def gen(n):
    for i in range(n):
        yield i     # By using this key word, we are not generating i here, but we are generating it by using gen() function

print(gen(10000000))
# THis prints: <generator object gen at 0x000002989036AC10>
# This didnot take up much RAM, python stored it as an information but didnot print it right now

# To generate the numbers, we'll do:
# for i in gen(10000000):
    # print(i)
    # This time, it will not take much RAM

# Testing Generators:-
ob1 = gen(10000000)
print(next(ob1)) # => 0
print(next(ob1)) # => 1
print(next(ob1)) # => 2
# ...
# => 9999999

# If we do like,
ob2 = gen(4)
print(next(ob2)) # => 0
print(next(ob2)) # => 1
print(next(ob2)) # => 2
print(next(ob2)) # => 3
# print(next(ob2)) # => Error of Stop Iteration will come

# num = 345
# for i in num:
#     print(i)    # => Error 'int' object is not iterable

num = "345"
for i in num:
    print(i)    # => It will work because 'String' object is iterable
    # => 3
    # => 4
    # => 5

iter1 = iter(num)
print(next(iter1)) # => 3
print(next(iter1)) # => 4
print(next(iter1)) # => 5
# print(next(iter1)) # => This will give error because the String has ended
