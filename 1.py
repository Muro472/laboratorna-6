a = [10,6,33,22,5,3]
i = 0
min = a[0]
length = len(a) - 1
while length > i:
    i += 1
    el = a[i]
    if el < min:
        min = el
print(min)