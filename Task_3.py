"""Дан список чисел: [1, 2, 3, 4, 5]. Используя функцию reduce, найдите произведение всех чисел в списке"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)
