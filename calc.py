# CALCULATOR
import math

from time import sleep


def addition(a, b):
    res = a + b
    return res


def subtraction(a, b):
    res = b - a
    return res


def multiplication(a, b):
    res = a * b
    return res


def division(a, b):
    if a == 0:
        print('Ділення на нуль недопустиме.')
        return None
    res = b / a
    return res


def steps(a, b):
    res = a ** b
    return res


def square_roots(a, b):
    res1 = math.sqrt(a)
    res2 = math.sqrt(b)
    return res1, res2


def cube_roots(a, b):
    res1 = a ** (1 / 3)
    res2 = b ** (1 / 3)
    return res1, res2


while True:
    print('''Це програма калькулятор! Виберіть одну з операцій з меню:
    1. Виконати додавання
    2. Виконати віднімання
    3. Виконати множення
    4. Виконати ділення
    5. Виконати зведення в ступінь
    6. Дізнатись квадратний корінь чисел
    7. Дізнатись кубічний корінь чисел
    8. Факторіал числа
    9. Вихід з програми
    ''')

    operation = input('Оберіть операцію або введіть "9" для завершення: ')

    if operation == '9':
        break

    if operation not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print('Такої операції не існує!')
        sleep(2)
        continue

    try:
        if operation == '8':
            num1 = int(input('Введіть число: '))
        if operation !='8':
            num1 = float(input('Введіть перше число: '))
            num2 = float(input('Введіть друге число: '))
        if operation in ['1', '2', '3', '4', '5']:
            result = 0
            if operation == '1':
                result = addition(num1, num2)
            elif operation == '2':
                result = subtraction(num1, num2)
            elif operation == '3':
                result = multiplication(num1, num2)
            elif operation == '4':
                result = division(num1, num2)
            elif operation == '5':
                result = steps(num1, num2)
            print(f'Результат: {result}')
        elif operation == '6':
            if num1 < 0 or num2 < 0:
                print("Квадратний корінь з від'ємного числа - комплексне число.")
            else:
                result1, result2 = square_roots(num1, num2)
                print(f'Квадратний корінь з {num1} дорівнює {result1}')
                print(f'Квадратний корінь з {num2} дорівнює {result2}')
        elif operation == '7':
            result1, result2 = cube_roots(num1, num2)
            print(f'Кубічний корінь з {num1} дорівнює {result1}')
            print(f'Кубічний корінь з {num2} дорівнює {result2}')
        elif operation == '8':
            fac = math.factorial(num1)
            print(f"Факторіал числа {num1} = {fac} ")
        sleep(2)

    except ValueError:
        print('Некоректне введення числа.')
        sleep(2)
