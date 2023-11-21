# 2. Дана действительная матрица размером n х m, все элементы которой различны.
# В каждой строке выбирается элемент с наименьшим значением.
# Если число четное, то заменяется нулем, нечетное -единицей. Вывести на экран новую матрицу.


def replace_min(matrix):
    new_matrix = []

    for row in matrix:
        min_value = min(row) # Находим мин. значение в строке
        new_row = [] # Создаем новую строку
        for elem in row:
            if elem == min_value: # Если элемент равен минимальному
                elem = elem % 2 # То заменяем его по условию

            new_row.append(elem) # Добавляем элемент в новую строку
        new_matrix.append(new_row)

    return new_matrix


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

new_matrix = replace_min(matrix) # Вызов фукнции замены наим. знач

print("Измененная матрица:")
print_matrix(new_matrix)