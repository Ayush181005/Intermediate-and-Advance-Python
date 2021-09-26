sampleList = ['chalk', 'duster', 'board', 'pen']
# => chalk and duster and board and pen
for item in sampleList:
    if item != 'pen':
        print(item + " and ", end="")
    else:
        print(item)

print(' and '.join(sampleList))