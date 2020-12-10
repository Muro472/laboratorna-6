a = [10,6,33,-22,5,3]
b = []
for i in range(len(a)):
        if a[i] > 0:
            b.append(a[i])
print(min(b))
