l1 = [3, 4, 5, 7, 8, 9, 32, 34, 56, 3]
print(l1[1:5]) # 1 to 5              => [4, 5, 7, 8]
print(l1[1:71]) # 1 to 71            => [4, 5, 7, 8, 9, 32, 34, 56, 3]
print(l1[1:]) # 1 to end             => [4, 5, 7, 8, 9, 32, 34, 56, 3]
print(l1[0:]) # 0 to end             => [3, 4, 5, 7, 8, 9, 32, 34, 56, 3]
print(l1[:5]) # start to 5           => [3, 4, 5, 7, 8]
print(l1[-2:5]) # -2 to 5            => []
print(l1[-2:-5]) # -2 to -5          => []
print(l1[-5:-2]) # -5 to -2          => [9, 32, 34]
print(l1[-2:]) # -2 to end           => [56, 3]
print(l1[:-2]) # -2 to end           => [3, 4, 5, 7, 8, 9, 32, 34]
print(l1[::2]) # Alternate 2         => [3, 5, 8, 32, 56]
print(l1[::3]) # Alternate 3         => [3, 7, 32, 3]
print(l1[::-3]) # Alternate 3        => [3, 32, 7, 3]
print(l1[::-1]) # Reversing the List => [3, 56, 34, 32, 9, 8, 7, 5, 4, 3]