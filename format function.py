# In C, in printf we do %d/%c/%f, format function is like that only

users = ["Ayush", "Shrey", "Maanit", "Jaimit"]
computers = ["Raspberry pi", "Android", "Apple", "Windows"]

for i in range(0, len(users)):
    print("Computer used by", users[i], "is", computers[i])

print("---------------------------------------------------")

for i in range(0, len(users)):
    template = "Computer used by {} is {}".format(users[i], computers[i])
    print (template)
    # OR
    template = "Computer used by {} is {}" # By default these are 0 and 1
    print(template.format(users[i], computers[i]))
    # If we make that 1 and 0:-
    template = "Computer used by {1} is {0}"
    print(template.format(users[i], computers[i]))  # Opposite will be printed