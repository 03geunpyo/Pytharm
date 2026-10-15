numbers = [1, 2, 2, 5, 3, 4, 3, 5, 1, 6]
result = []

for n in numbers:
    if n not in result:
        result.append(n)

print(result)