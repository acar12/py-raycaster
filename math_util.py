import math

next_num = lambda x: math.floor(x) + 1 - x
prev_num = lambda x: x - 1 if x % 1 == 0 else math.floor(x)

def x_step(px, dir):
    if math.cos(dir) > 0:
        return next_num(px) - px
    else:
        return prev_num(px) - px

def y_step(py, dir):
    if math.sin(dir) > 0:
        return next_num(py) - py
    else:
        return prev_num(py) - py

def complete_vec(dir, *, px=None, py=None):
    if px: # get py
        scl = px / math.cos(dir)
        return scl * math.sin(dir)
    else: # get px
        scl = py / math.sin(dir)
        return scl * math.cos(dir)

def vec_add(a, b):
    return (a[0] + b[0], a[1] + b[1])