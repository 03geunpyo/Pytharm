list1 = [1, 0, 1]
list2 = [1, 1, 2]

result = sum(a * b for a, b in zip(list1, list2))

print(f"{list1} * {list2} = {result}")