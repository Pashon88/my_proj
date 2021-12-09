def fn2(**c):
    z = 1
    for x in c.values():
        z = z * x
    return z
default_args = {'c': 5, 'd': 2, 'e': 20}
print(fn2(**default_args))