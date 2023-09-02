import math

next_num = lambda x: math.floor(x) + 1 - x
prev_num = lambda x: x - 1 if x % 1 == 0 else math.floor(x)
sign = lambda x: -1 if x < 0 else 1

def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1]

def vec_scl(a, b, scl):
    return a * scl, b * scl