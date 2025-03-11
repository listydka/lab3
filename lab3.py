import random

# Функция для проверки простое ли число
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Функция для подсчета простых чисел в нечетных столбцах матрицы
def count_primes_in_odd_columns(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i]), 2):  # нечетные столбцы
            if is_prime(matrix[i][j]):
                count += 1
    return count

# Функция для подсчета нулевых элементов в четных строках матрицы
def count_zeros_in_even_rows(matrix):
    count = 0
    for i in range(0, len(matrix), 2):  # четные строки
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                count += 1
    return count

# Вводим значения K и N
K = int(input("Введите K="))
N = int(input("Введите N="))

# Проверим, что N четное (для корректного деления на 2)
if N % 2 != 0:
    print("Ошибка: N должно быть четным числом.")
    exit()

# Инициализация подматриц
D = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
E = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
C = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]
B = [[random.randint(-10, 10) for _ in range(N // 2)] for _ in range(N // 2)]

# Формируем матрицу A
A = [D[i] + E[i] for i in range(N // 2)]  # Добавляем D и E
A += [C[i] + B[i] for i in range(N // 2)]  # Добавляем C и B

# Выводим матрицу A
print("Матрица A:\n", A, "\n")

# Подсчитываем количество простых чисел в нечетных столбцах области 2
primes_in_odd_columns = count_primes_in_odd_columns(C)

# Подсчитываем количество нулевых элементов в четных строках области 3
zeros_in_even_rows = count_zeros_in_even_rows(C)

# Инициализация матрицы F в зависимости от условий
if primes_in_odd_columns > zeros_in_even_rows:
    # Меняем области симметрично (обмен 1 и 3 областями)
    for i in range(N // 4):
        for j in range(N // 2 - 1 - i):
            C[i][j], C[N // 2 - 1 - i][N // 2 - 1 - j] = C[N // 2 - 1 - i][N // 2 - 1 - j], C[i][j]

    F = [D[i] + E[i] for i in range(N // 2)]  # F = D + E
    F += [C[i] + B[i] for i in range(N // 2)]  # F = C + B
else:
    # Меняем области несимметрично (меняем B и C местами)
    F = [D[i] + C[i] for i in range(N // 2)]  # F = D + C
    F += [E[i] + B[i] for i in range(N // 2)]  # F = E + B

# Выводим матрицу F
print(f'Матрица F:\n {F}\n')

# Проверяем размеры матриц F и A
if len(A[0]) != len(F):
    print("Ошибка: Размеры матриц для умножения не совпадают.")
    exit()

# Инициализация матрицы G для вычислений
G = [[0] * N for _ in range(N)]

# Выполняем операцию F * A
for i in range(N):
    for j in range(N):
        for k in range(N):
            G[i][j] += F[i][k] * A[k][j]

print(f'\nF * A:\n{G}')

# Транспонируем матрицу A и умножаем на K
H = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        H[i][j] = A[j][i] * K

print(f'\nK * A^T:\n{H}')

# Вычисляем финальный результат (F * A - K * A^T)
for i in range(N):
    for j in range(N):
        G[i][j] -= H[i][j]

print(f'\nКонечный результат:\n{G}')
