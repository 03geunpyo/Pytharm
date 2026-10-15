def deco2_add(type):
    def decorator(func):
        def wrapper(a, b):
            result = func(a, b)
            if type == "math":
                return f"{a} + {b} = {result}"
            elif type == "word":
                return f"The sum of {a} and {b} is {result}"
            return result
        return wrapper
    return decorator