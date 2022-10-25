rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()