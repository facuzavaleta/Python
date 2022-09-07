def sum_square(x, y):
    return x + y ** 2

def module(v):
    from functools import reduce
    return reduce(sum_square, v, 0) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))