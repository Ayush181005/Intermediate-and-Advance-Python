# try:
#     open("this.txt")
# except Exception as e:
#     print(e)
# print("program zinda hai")

# multiple Exceptions:-
'''
try:
    open("this.txt", 'r')
except EOFError as e:
    print("EOF Error")
except IOError as e:
    print("IO Error")
finally:
    print("This will be printed irrespective of the exception occurance")
'''

try:
    print("I will be printed if no exception, and I will throw exception if any problem")
except Exception as e:
    print("I will be printed if any exception is there, when try block fails")
else:
    print("I will be printed only if there is no exception, use this to run code which should only execute if there is no exception")
finally:
    print("I will be printed in every case")
