n = int(input())
matrix = []


for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

a = [matrix[j][k] for k in range(n) for j in range(n) if j < k and j < n - 1 - k]
b = [matrix[j][k] for k in range(n) for j in range(n) if j < k and j > n - 1 - k]
c = [matrix[j][k] for k in range(n) for j in range(n) if j > k and j > n - 1 - k]
d = [matrix[j][k] for k in range(n) for j in range(n) if j > k and j < n - 1 - k]
print(f'Верхняя четверть: {sum(a)}', f'Правая четверть: {sum(b)}', f'Нижняя четверть: {sum(c)}', f'Левая четверть: {sum(d)}', sep='\n')
