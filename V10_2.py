#2. Расположить столбцы матрицы D[M, N] в порядке возрастания элементов k-й строки (1 <= k <= М).

def sort_columns(matrix, k):
    sorted_columns = sorted(range(len(matrix[0])), key=lambda i: matrix[k - 1][i]) # Получаем индексы столбцов, отсортированных по элементам k-й строки

    sorted_matrix = [] # Создаем новую матрицу с отсортированными столбцами
    for row in range(len(matrix)):
        new_row = [] # Создаем новую строку массива
        for col in sorted_columns:
            new_row.append(matrix[row][col]) # Заполняем новую строку элементами из отсортированных столбцов

        sorted_matrix.append(new_row)

    return sorted_matrix

def print_matrix(matrix): # Процедура вывода матрицы в консоль
    for row in matrix:
        print(row)


n = int(input("Введите n:"))
m = int(input("Введите m:"))
k = int(input("Введите k: "))
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(input(f"Введите [{i},{j}] элемент: "))
        row.append(elem)
    matrix.append(row)


result_matrix = sort_columns(matrix, k)

# Выводим исходную и отсортированную матрицы
print("Исходная матрица:")
print_matrix(matrix)

print("\nМатрица с отсортированными столбцами:")
print_matrix(result_matrix)
