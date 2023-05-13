import math
from itertools import zip_longest
from math import factorial

import numpy as np


def q_calc(x, x0, h):
    return (x - x0) / h


def q_func_f(q, n):
    result = q
    count = 1
    i = 1
    while i < n:
        if i % 2 != 0:
            result *= (q - count)
        else:
            result *= (q + count)
            count += 1
        i += 1
    return result


def q_func_f(q, n):
    result = q
    count = 1
    i = 1
    while i < n:
        if i % 2 != 0:
            result *= (q - count)
        else:
            result *= (q + count)
            count += 1
        i += 1
    return result


def q_func_s(q, n):
    result = q
    count = 1
    i = 1
    while i < n:
        if i % 2 != 0:
            result *= (q + count)
        else:
            result *= (q - count)
            count += 1
        i += 1
    return result


def del_y(y):
    return [np.diff(y, n=d) for d in range(1, len(y))]

def recurs(data, lst):
    if len(lst) == 1:  # ещё можно добавить проверку на пустой список
        return
    temp = []
    for i in range(len(lst) - 1):
        temp.append(lst[i + 1] - lst[i])
    data.append(temp)
    recurs(data, temp)

#http://virtet.gsu.by/mod/resource/view.php?id=190

def f_gauss(x, y, h, x_f, n):
    q = (x_f - x[int(len(x) / 2)])/h
    print(q)
    y_dif = del_y(y)
    for i in range(len(y_dif)):
        print(y_dif[i])
    result = y[int(len(x) / 2)]
    for i in range(1, n):
        value = (q_func_f(q, i) / factorial(i)) * y_dif[i-1][math.floor((len(y_dif[i-1]))/2) - math.floor(i / 2)]
        result += value
        print(i, value)
    return result


def s_gauss(x, y, h, x_f, n):
    q = (x_f - x[int(len(x) / 2)]) / h
    print(q)
    y_dif = del_y(y)
    for i in y_dif:
        print(i)
    result = y[int(len(x) / 2)]
    for i in range(n, 0, -1):
        value = (q_func_f(q, i) / factorial(i)) * y_dif[i-1][math.floor((len(y_dif[i-1]))/2) - math.ceil(i / 2)]
        result += value
        print(i, value)
    return result
