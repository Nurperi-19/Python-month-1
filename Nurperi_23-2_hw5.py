# Создать словарь: ключом будет домен страны, значениями будут цвета флага страны содержащиеся в сэте,
#  например: 'kg': {'red', 'yellow'}
# Должно быть несколько примеров из любых стран.
flags = {
    'eg': {'yellow', 'white', 'black', 'red'},
    'tj': {'yellow', 'white', 'red', 'green'},
    'tm': {'yellow', 'white', 'red', 'green'},
    'br': {'yellow', 'white', 'blue', 'green'},
    'cy': {'yellow', 'white', 'green'},
    'be': {'yellow', 'black', 'red'},
    'de': {'yellow', 'black', 'red'},
    'tz': {'yellow', 'black', 'blue', 'green'},
    'kg': {'yellow', 'red'},
    'am': {'yellow', 'red', 'blue'},
    'mn': {'yellow', 'red', 'blue'},
    'ro': {'yellow', 'red', 'blue'},
    'et': {'yellow', 'red', 'blue', 'green'},
    'ru': {'white', 'red', 'blue'},
    'tr': {'white', 'red'}
}
# Создать цикл с возможностью выхода, в каждом круге которого будет запрашиваться цвет у пользователя

while flags:
    word = input("Enter the color [Type 'q' to quit]: ")
    if word == 'q':
        print('The program is completed')
        break
    for domain, flag in flags.items():
        if word in flag:
            print(domain)   # При вводе одного цвета должны отобразиться все домены стран имеющие этот цвет

    else:
        print('Try to enter a different color')  # Если введенного цвета нет в заданных флагах, вывести соответствующее
                                                 # сообщение на экран и продолжать цикл

# При вводе более одного цвета должны отобразиться только домены стран имеющие все указанные цвета