def do_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(do_operation(add, 2, 3))
print(do_operation(sub, 5, 2))

print(do_operation(lambda x, y: x + y, 2, 3))
print(do_operation(lambda x, y: x - y, 5, 2))