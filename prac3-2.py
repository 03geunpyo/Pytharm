def min_max(lst):
    return (min(lst), max(lst))

numbers = list(map(int, input("정수들을 띄어쓰기로 입력: ").split()))
result = min_max(numbers)
print(result)