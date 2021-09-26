import bisect

number = 5
a = [1, 2, 4, 6, 7, 8, 9, 34]

# Insert the number(5) in such a way that the list remains sorted

print (bisect.bisect(a, number))    # => 3, it will give the index of the position where we need to add number
# Bisect function donot check whether the list is sorted or not
bisect.insort(a, number)
print(a)    # This will insert the number in correct index
