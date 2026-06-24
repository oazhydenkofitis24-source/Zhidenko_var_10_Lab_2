# Введення розмірів матриці
m = int(input("Введіть кількість рядків m: "))
n = int(input("Введіть кількість стовпців n: "))

# Введення чисел через пропуск
numbers = input("Введіть цілі числа через пробіл: ").split()

# Перевірка коректності введення
if len(numbers) != m * n:
    print("Помилка: кількість чисел не відповідає розмірам матриці!")
else:
    # Перетворення у двовимірний список
    matrix = []
    for i in range(m):
        row = [int(numbers[i*n + j]) for j in range(n)]
        matrix.append(row)

    print("Початкова матриця:")
    for row in matrix:
        print(row)

    # Відображення відносно горизонтальної осі
    flipped = matrix[::-1]

    print("Матриця після відображення:")
    for row in flipped:
        print(row)

input()
