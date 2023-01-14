# Пользователь загадывает число до 100 только целое число (int), программа должна угадать это число
# за минимальное количество попыток.
print('Guess your number from 1 to 100 (only integers!)')

with open('results.txt', 'w', encoding='UTF-8') as file:
    file.write('Results/Результаты')

first_half = 1
second_half = 100
attempt = 0

while True:     # Программа должна работать в бесконечном цикле, пытаясь угадать число
    try:
        x = (first_half + second_half)//2
        print('Is your number 1-LARGER, 2-SMALLER or 3-EQUAL',  x,)     # Пользователь должен отвечать программе
        user_answer = int(input('? '))                                  # «да, больше или меньше»
        if user_answer == 3:
            attempt += 1
            with open('results.txt', 'a', encoding='UTF-8') as file:
                file.write(f"\nNumber of attempts/Количество попыток"
                           f": {attempt} \nHidden number/Загаданное число: {x}")
            print('I won! Thanks for playing!')
            break                                         # Если программа угадывает число, записать в файл results.txt
        elif user_answer == 1:                            # количество попыток, список попыток  и загаданное число,
            first_half = x                                # затем выйти из цикла.
            attempt += 1
            with open('results.txt', 'a') as file:
                file.write(f"\nAttempt: {x} (Larger)")
        else:
            second_half = x
            attempt += 1
            with open('results.txt', 'a') as file:
                file.write(f"\nAttempt: {x} (Smaller)")
    except:
        print('Enter only integers! (Введите только целые числа!)')  # При неверном вводе пользователя продолжать цикл
                                                                     # с подсказкой корректного ввода.
