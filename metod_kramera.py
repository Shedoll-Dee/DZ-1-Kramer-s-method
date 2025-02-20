import random


def convert_to_float_or_complex(numbers_input: str):
        while "  " in numbers_input:
            numbers_input = numbers_input.replace("  ", " ")

        if " " in numbers_input:
            numbers_input = [float(number) for number in numbers_input.split()]
            return complex(numbers_input[0], numbers_input[1])

        else:
            return float(numbers_input)
    

def determinant_of_the_matrix(n: int, matrix: list[list]):
    if n == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return determinant
    
    determinant = 0
    for i in range(n):
        new_matrix = [matrix[j][0: i] + matrix[j][i+1: n] for j in range(1, n)]
        if i % 2 == 0:
            sign = 1
        else:
            sign = -1
        determinant += (sign * matrix[0][i] * determinant_of_the_matrix(n-1, new_matrix))
    return determinant


def metod_kramera(n: int, matrix: list[list], column_of_free_members: list):
    determinant = determinant_of_the_matrix(n, matrix)
    if determinant != 0:
        print("Решение:")
        for i in range(n):
            new_matrix = [matrix[j][0: i] + [column_of_free_members[j]] + matrix[j][i+1: n] for j in range(n)]
            new_determinant = determinant_of_the_matrix(n, new_matrix)
            print(f"x{i+1} = {new_determinant / determinant}")

    else:
        print("Нет решения, определитель матрицы равен 0")


n = int(input("Введите величину расширенной матрицы n x (n + 1): "))
matrix = []
column_of_free_members = []
answer = input("Хотите сгенерировать случайные значения для матрицы? В ней будут только целые числа от -10 до 10 включительно.\n(Да/Нет) ").lower()

if answer == "да":
    for _ in range(n):
        matrix.append([random.randint(-10, 10) for i in range(n)])
        column_of_free_members.append(random.randint(-10, 10))
else:
    if answer != "нет":
        print("Будем считать, что вы сами хотите ввести все значения для матрицы :)")
    print("Если вы хотите ввести комплексное число, то напишите два действительных числа через пробел: сначала действительная часть, потом мнимая.")
    for i in range(n):
        string_of_numbers = []

        for j in range(n):
            numbers_input = input(f"Строка {i+1} столбец {j+1}: ").strip()
            numbers_input = convert_to_float_or_complex(numbers_input)
            string_of_numbers.append(numbers_input)

        matrix.append(string_of_numbers)
        number_input = input(f"Свободный член матрицы {i+1}: ").strip()
        number_input = convert_to_float_or_complex(number_input)
        column_of_free_members.append(number_input)

print("\nВаша расширенная матрица:")
for i in range(n):
    print(matrix[i], end=" ")
    print(column_of_free_members[i])

if n == 1 and matrix[0] != 0:
    print(f"Решение: \nx = {column_of_free_members[0]/matrix[0][0]}")

elif n == 1 and matrix[0] == 0:
    print("Нет решения")

else:
    metod_kramera(n, matrix, column_of_free_members)