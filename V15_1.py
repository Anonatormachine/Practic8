# 1. Определить номера строк матрицы R[M, N], хотя бы один элемент которых равен с, и элементы этих строк умножить на d


def find_and_multiply_rows(matrix, c, d):
    new_matrix = []

    for row in matrix:
        if c in row:
            row = [elem * d for elem in row]

        new_matrix.append(row)

    return new_matrix

def print_matrix(matrix): # Процедура вывода матрицы в консоль
    for row in matrix:
        print(row)


n = int(input("Введите n:"))
m = int(input("Введите m:"))

c = int(input("Введите c:"))
d = int(input("Введите d:"))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(input(f"Введите [{i},{j}] элемент: "))
        row.append(elem)
    matrix.append(row)



print("Исходная матрица:")
print_matrix(matrix)

result_matrix = find_and_multiply_rows(matrix, c, d) # Находим строки, содержащие хотя бы один элемент равный c, и умножаем их на d

print("\nМатрица с умноженными строками:")
print_matrix(result_matrix)
