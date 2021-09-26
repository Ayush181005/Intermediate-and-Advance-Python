a = ['CodeWithHarry', 'T Series', 'Mixer Grinder', 'Pen']

i = 0
for item in a:
    i += 1
    if i % 2 == 0:
        print(item)

for i, item in enumerate(a):
    print(i, item)

for i, item in enumerate(a):
    if (i+1)%2 == 0:
        print(i, item)
