# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

while True: # Создаю бесконечный цикл, для возможности вернуть пользователя в начало, если ввод был неверен

    user_input = input('Введите целое число, которое хотите преобразовать: ') # Ввод данных пользователем

    res = '' # Переменная для записи ответа

    # Проверка на ввод корректных данных
    try:
        user_input = int(user_input) # Пробует преобразовать введеные пользователем данные в целое число
    except:
        print('Что-то не так, попробуйте ещё раз') # Если не удалось, выводит сообщение
        continue # И возвращает в начало

    # Создание переменной для проверки результата и красивого вывода результата
    _check = user_input

    while user_input: # Создание цикла, пока переменная не будет меньше 0
        # Проверка, чему равен остаток числа, для определения буква в шестнадцатиричной системе счисления
        if user_input % 16 == 10:
            res = 'a' + res
            user_input //= 16
        elif  user_input % 16 == 11:
            res = 'b' + res
            user_input //= 16
        elif  user_input % 16 == 12:
            res = 'c' + res
            user_input //= 16
        elif  user_input % 16 == 13:
            res = 'd' + res
            user_input //= 16
        elif  user_input % 16 == 14:
            res = 'e' + res
            user_input //= 16
        elif  user_input % 16 == 15:
            res = 'f' + res
            user_input //= 16
        else: # Если остаток не является одной из букв
            res = f'{user_input % 16}' + res # Остаток записывается в ответ
            user_input //= 16
    else: # Когда переменная становится меньше 0
        print(f'Число {_check} в шестнадцатиричной системе счисления, равно 0x{res}') # Выводим ответ
        # Проверка с помощью встроенной функции hex
        print(f'Проверка: {hex(_check)}')
        break # Для выхода из бесконечного цикла
