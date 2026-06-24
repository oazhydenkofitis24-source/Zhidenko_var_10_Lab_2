import random

# Генерація масиву з 20 випадкових цілих чисел у діапазоні від 1 до 100
arr = [random.randint(1, 100) for _ in range(20)]
print("Згенерований масив:", arr)

# Вибір чисел, кратних 11
multiples = [x for x in arr if x % 11 == 0]

# Сортування у порядку спадання
multiples.sort(reverse=True)

# Вивід результату
print("Числа кратні 11 у порядку спадання:", multiples)
input()
