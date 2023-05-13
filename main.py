import math
from Gauss import f_gauss,s_gauss

import numpy as np
from matplotlib import pyplot as pl


def func(a, b, i):
    #return math.log(i)**(a/b)*math.sin(i)
    return i**2
if __name__ == '__main__':
    a = 13
    b = 4
    k = 3
    c = 2
    d = 20
    h = 1
    #x, y = func(a, b, k, c, d,h)

    x = []
    y = []
    i = c
    while i < d+h:
        x.append(i)
        y.append(func(a, b, i))
        i += h

    print(x)
    print(y)
    print("###############################")
    x_f = 11.35
    if x_f > x[int(len(x) / 2)]:
        y_f = f_gauss(x, y, h, x_f,15)
    else:
        y_f = s_gauss(x, y, h, x_f, 12)

    y_c = func(a, b, x_f)
    print(x[int(len(x) / 2)])
    print(x_f, y_f)
    print(x_f, y_c)
    print(math.floor(x_f),func(a, b, math.floor(x_f)))
    print(math.ceil(x_f), func(a, b, math.ceil(x_f)))
    print("%", math.fabs((y_c-y_f)/y_c)*100)
    pl.plot(y, label='main')
    pl.scatter(x_f, y_f, color='r')
    pl.grid()
    pl.show()
#погрешности по эпсилон4
