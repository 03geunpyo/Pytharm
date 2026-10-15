x = 10

def test():
    global x
    print(x)
    x = 20

test()
print(x)