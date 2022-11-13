n, m  = [int(i) for i in input().split()]

matrix1 = [[(i + j) % m + 1 for j in range(m)] for i in range(n)]

for k in range(n):
    for l in range(m):
        print(str(matrix1[k][l]).ljust(3), end=' ')
    print()
