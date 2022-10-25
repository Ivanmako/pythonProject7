n, m = int(input()), int(input())
matrix = []
for i in range(n):
    temp = [[(num) for num in input().split()] for j in range(m)]
    matrix.append(temp)

for i in matrix:
    for j in i:
        print(*j, end=' ')
    print()
print()

for k in range(len(matrix[0])):
    for l in range(len(matrix)):
        print(*matrix[l][k], end=' ')
    print()
