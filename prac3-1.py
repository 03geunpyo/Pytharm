def calc(*args, op="+"):
    if op == "+":
        return sum(args)
    elif op == "*":
        result = 1
        for num in args:
            result *= num
        return result
    return 0