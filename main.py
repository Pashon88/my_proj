def fn2(**c):
    z = 1
    z != 100
    for x in c.values():
        z = z * x
    return z
default_args = {'c': 5, 'd': 2, 'e': 20, 'p': 50, 's': 100}
print(fn2(**default_args))

print("it's OK")