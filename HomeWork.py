# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# Импорт для проверки
from fractions import Fraction

# Ввод данных пользователя
str1 = input('Введите дробь в виде a/b: ')
str2 = input('Введите дробь в виде a/b: ')

# Разбитие введенных данных на числители и знаминатели
number1_str1 = int(str1.split('/')[0]) # Числитель первой строки
number2_str1 = int(str1.split('/')[1]) # Значенитель перой строки
number1_str2 = int(str2.split('/')[0]) # Числитель второй строки
number2_str2 = int(str2.split('/')[1]) # Знаменатель второй строки

# Сложение дробей
if number2_str1 != number2_str2: # Проверка на равенство знаменателей
    sum1 = (number1_str1 * number2_str2) + (number1_str2 * number2_str1) # Нахождение числителя при назных знаменателях
    sum2 = number2_str1 * number2_str2 # Нахождение знаменателя при разных знаменателях
else:
    sum1 = number1_str1 + number1_str2 # Нахождение числителя при одинаковых знаменателях
    sum2 = number2_str1 # Знаменатель при сложении дробей с одинаковыми знаменателями

# Функция сокращения дробей при влзможности
def reduction(number1, number2):
    for idx in range(2, number1 + 1): # idx - число, на которе могут делиться числитель и знаменатель при сокращении
        while number1 % idx == 0 and number2 % idx == 0: # Проверка, можно ли сократить дробь
            number1 //= idx # Сокращение числителя
            number2 //= idx # Сокращение знаменателя
    return number1, number2 # Возврат сокращенного числите и знаменателя

if sum1 == sum2: # Проверка на равенство числителя и знаметателя
    print(f'{str1} + {str2} = {1}') # Если числитель и знаменатель равны, сумма будет равна 1
else:
    sum_lst = reduction(sum1, sum2) # Иначе пробуем сократить дробь
    print(f'{str1} + {str2} = {sum_lst[0]}/{sum_lst[1]}') # Выводим дробь после сложения и сокращения

product1 = number1_str1 * number1_str2 # Нахождение числителя при умножении дробей
product2 = number2_str1 * number2_str2 # Нахождение знаменателся при умножении дробей

if product1 == product2: # Проверка на равенство числителя и знаменателя
    print(f'{str1} * {str2} = {1}') # Если равны, произведение равно 1
else:
    product_lst = reduction(product1, product2) # Иначе пробуем сокраить дробь
    print(f'{str1} * {str2} = {product_lst[0]}/{product_lst[1]}') # Вывод произведения дробей

# Проверка
print(f'Сумма: {Fraction(number1_str1, number2_str1) + Fraction(number2_str1, number2_str2)}')
print(f'Произведение: {Fraction(number1_str1, number2_str1) * Fraction(number2_str1, number2_str2)}')
