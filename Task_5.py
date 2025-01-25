"""Дан список строк: ["apple", "banana", "cherry", "date", "elderberry"]
Необходимо создать новый список, содержащий только те слова, длина которых больше 5 символов, и преобразовать их в верхний регистр"""

words = ["apple", "banana", "cherry", "date", "elderberry"]
result = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 5, words)))
print(result)
