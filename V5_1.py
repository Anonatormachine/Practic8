# 1. Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.

def sort_matrix_row(matrix):
    for row in matrix:
        row.sort() 

def print_matrix(matrix): 
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


print("Исходная матрица:")
print_matrix(matrix)

sort_matrix_row(matrix)

print("Упорядоченная матрица:") 
print_matrix(matrix)
