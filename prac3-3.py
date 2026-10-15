def count_vowel(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

text = input("문자열 입력: ")
result = count_vowel(text)
print(result)