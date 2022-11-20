n, m  = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
num = 0
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                num += 1
                matrix[i][j] = num

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()
