a = [10,6,0,22,5,3]
n = len(a)
i = 0
zero = []
not_zero = []
while n > i:
    elem = a[i]
    i += 1
    if elem == 0:
        zero = zero + [0]
        continue
    not_zero = not_zero + [elem]
print(zero + not_zero)