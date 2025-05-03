a = [3, 4, 5, 5, 7]

for i in range(len(a)):
    while i == 5:
        a.pop(i)
    if len(a) == 0:
        break
    print(i)