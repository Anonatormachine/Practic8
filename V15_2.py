# 2. Среди тех строк целочисленной матрицы, которые содержат только нечетные элементы, найти строку с максимальной суммой модулей элементов.

def is_odd_row(row): # Проверяем все ли элементы строки нечетные
    for elem in row:
        if elem % 2 == 0:
            return False
    return True

def find_max_sum_row(matrix):
    max_sum = 0
    row_index = None

    for i, row in enumerate(matrix):
        if is_odd_row(row): # Если строка содержит только нечетные элементы
            row_sum = sum(map(abs, row)) # Находим сумму модулей элементов
            if row_sum > max_sum: # Если сумма строки больше ранее найденной
                max_sum = row_sum # Заменяем максимальную сумму строки
                row_index = i # Заменяем индекс строки

    return row_index

n = int(input("Введите n:"))
m = int(input("Введите m:"))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(input(f"Введите [{i},{j}] элемент: "))
        row.append(elem)
    matrix.append(row)


row_index = find_max_sum_row(matrix) # Находим строку с максимальной суммой модулей элементов, состоящих из нечетных чисел

# Выводим результат
if row_index is not None:
    print(f"Строка с максимальной суммой модулей элементов состоит только из нечетных чисел: {matrix[row_index]}")
else:
    print("Нет строк, состоящих только из нечетных элементов.")
