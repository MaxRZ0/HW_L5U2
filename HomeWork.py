while True:

    user_input = input('Введите целое число, которое хотите преобразовать: ')
    res = ''

    try:
        user_input = int(user_input)
    except:
        print('Что-то не так, попробуйте ещё раз')
        continue

    while user_input:
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
        else:
            res = f'{user_input % 16}' + res
            user_input //= 16
    else:
        print(f'0x{res}')
        break
