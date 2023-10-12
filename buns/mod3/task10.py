size = int(input("Введите размерность квадратной матрицы: "))
matrix = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(j + 1)
    matrix.append(row)

for row in matrix: print(row)
print()

for i in range(size):
    for j in range(i, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix: print(row)