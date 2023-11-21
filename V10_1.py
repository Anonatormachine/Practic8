#1. Найти максимальный среди всех элементов тех строк заданной матрицы, которые упорядочены (либо по возрастанию, либо по убыванию)


def is_sorted_row(row): # Проверяем является ли строка отсортированной (либо по возрастанию, либо по убыванию)
    sort_row = sorted(row)
    reverse_row = sort_row.copy()
    reverse_row.reverse()
    return  row == sort_row or row == reverse_row


def find_max(matrix):
    max_value = float("-inf") # Задаем минимальному элементу значение минус бесконечности

    for row in matrix:
        if is_sorted_row(row): # Проверяем является ли строка отсортированной (либо по возрастанию, либо по убыванию)
            row_max = max(row) # Находим максимальный элемент строки
            if row_max > max_value: # Если максимальный элемент строки больше найденного прежде элемента
                max_value = row_max

    return max_value


def print_matrix(matrix): # Процедура вывода матрицы в консоль
    for row in matrix:
        print(row)


n = int(input("Введите n:"))
m = int(input("Введите m:"))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(input(f"Введите [{i},{j}] элемент: "))
        row.append(elem)
    matrix.append(row)


print("Исходная матрица:") # Выводим исходную матрицу
print_matrix(matrix)

max_value = find_max(matrix) # Вызов фукнции для поиска максимального значения

if max_value != float("-inf"):
    print(f"Максимальный элемент в отсортированных строках: {max_value}")
else:
    print("В массиве нет ни одной отсортированной строки")