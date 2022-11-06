n = input()
x = int('abcdefgh'.find(n[0]))
y = int('87654321'.find(n[1]))
matrix = [['.' for _ in range(8)] for _ in range(8)]

matrix[x + 1][y] = 'N'
for k in range(8):
    for l in range(8):
        if (y-l)*(x-k)==2 or (y-l)*(x-k)==-2:
            matrix[k][l] = '*'

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()