def deco_add(func):
    def wrapper(a, b):
        result = func(a, b)
        return f"{a} + {b} = {result}"
    return wrapper

@deco_add
def add(a, b):
    return a + b

print(add(2, 4))