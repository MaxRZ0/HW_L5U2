from fractions import Fraction

str1 = input('Введите дробь в виде a/b: ')
str2 = input('Введите дробь в виде a/b: ')

number1_str1 = int(str1.split('/')[0])
number2_str1 = int(str1.split('/')[1])
number1_str2 = int(str2.split('/')[0])
number2_str2 = int(str2.split('/')[1])

if number2_str1 != number2_str2:
    sum1 = (number1_str1 * number2_str2) + (number1_str2 * number2_str1)
    sum2 = number2_str1 * number2_str2
else:
    sum1 = number1_str1 + number1_str2
    sum2 = number2_str1

def reduction(number1, number2):
    for idx in range(2, number1 + 1):
        while number1 % idx == 0 and number2 % idx == 0:
            number1 //= idx
            number2 //= idx
    return number1, number2

if sum1 == sum2:
    print(f'{str1} + {str2} = {1}')
else:
    sum_lst = reduction(sum1, sum2)
    print(f'{str1} + {str2} = {sum_lst[0]}/{sum_lst[1]}')

product1 = number1_str1 * number1_str2
product2 = number2_str1 * number2_str2

if product1 == product2:
    print(f'{str1} * {str2} = {1}')
else:
    product_lst = reduction(product1, product2)
    print(f'{str1} * {str2} = {product_lst[0]}/{product_lst[1]}')
