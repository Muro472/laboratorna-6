a = input('координати верктора a').split(' ')
b = input('координати вектора b').split(' ')
lengtha = len(a)
lengthb = len(b)
a_x = float(a[0])
a_y = float(a[1])
b_x = float(b[0])
b_y = float(b[1])
if (lengtha + lengthb) == 6:
    a_z = float(a[2])
    b_z = float(b[2])
    if (a_x / b_x) == (a_y / b_y) == (a_z / b_z):
        print('вектора паралельні')
    else:
        print('вектора не паралельні')
elif (lengtha + lengthb) == 4:
    if (a_x / b_x) == (a_y / b_y):
        print('вектора паралельні')
    else:
        print('вектора не паралельні')

else:
    print('неправильно введені дані')