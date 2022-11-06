n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

def check(): #Функция проверки списка на наличие всех чисел
    check_list = [matrix[i][j] for j in range(n) for i in range(n)] #генерируем список всех чифор основной матрицы, чтобы его потом сравнить
    matrix_num = [i for i in range(1, (n ** 2) + 1)] #генерируем список чисел по условию
    check_list.sort()
    if check_list == matrix_num:
        return True
    else:
        return False

def magick():
    matrix_magik = []
    for i in range(n):#Цикл добавления суммы элемантов по строкам
        matrix_magik.append(sum(matrix[i]))

    for j in range(n): #Цикл добавления суммы элемантов по столбцам
        elem = [matrix[k][j] for k in range(n)]
        matrix_magik.append(sum(elem))

    matrix_magik.append(sum([matrix[l][l] for l in range(n)])) #добавления суммы элемантов по главной диагонали
    matrix_magik.append(sum([matrix[h][n - h - 1] for h in range(n)])) #добавления суммы элемантов по второстепенной диагонали

    if exam_num(matrix_magik) and check():
        return 'YES'
    else:
        return 'NO'

def exam_num(matrix_magick): # Функция для проверки равности всех чисел в списке
    for i in range(1, len(matrix_magick)):
         if matrix_magick[i] != matrix_magick[i - 1]:
             return False
    return True

print(magick())


