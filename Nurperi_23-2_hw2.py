# Написать программу знаков зодиака.
print("your zodiac sign".title())
# Программа должна запрашивать у пользователя день,месяц рождения, затем выводить на экран соответствующий знак зодиака
birthday = input("Enter your birthday: ")

date = int(birthday[0:2])   # Создать возможность вводить данные в одной строке с любым символом разделяющим день,месяц
month = int(birthday[-2:])  # Решить задание с помощью срезов

if (21 <= date <= 31 and month == 1) or (1 <= date <= 19 and month == 2):
    print("Your zodiac sign is Aquarius (Водолей)")
elif (20 <= date <= 28 and month == 2) or (1 <= date <= 20 and month == 3):
    print("Your zodiac sign is Pisces (Рыбы)")
elif (21 <= date <= 31 and month == 3) or (1 <= date <= 20 and month == 4):
    print("Your zodiac sign is Aries (Овен)")
elif (21 <= date <= 30 and month == 4) or (1 <= date <= 21 and month == 5):
    print("Your zodiac sign is Taurus (Телец)")
elif (22 <= date <= 31 and month == 5) or (1 <= date <= 21 and month == 6):
    print("Your zodiac sign is Gemini (Близнецы)")
elif (22 <= date <= 30 and month == 6) or (1 <= date <= 22 and month == 7):
    print("Your zodiac sign is Cancer (Рак)")
elif (23 <= date <= 31 and month == 7) or (1 <= date <= 21 and month == 8):
    print("Your zodiac sign is Leo (Лев)")
elif (22 <= date <= 31 and month == 8) or (1 <= date <= 23 and month == 9):
    print("Your zodiac sign is Virgo (Дева)")
elif (24 <= date <= 30 and month == 9) or (1 <= date <= 23 and month == 10):
    print("Your zodiac sign is Libra (Весы)")
elif (24 <= date <= 31 and month == 10) or (1 <= date <= 22 and month == 11):
    print("Your zodiac sign is Scorpio (Скорпион)")
elif (23 <= date <= 30 and month == 11) or (1 <= date <= 22 and month == 12):
    print("Your zodiac sign is Sagittarius (Стрелец)")
elif (23 <= date <= 31 and month == 12) or (20 >= date >= 1 == month):
    print("Your zodiac sign is Capricorn (Козерог)")
else:
    print("Please enter your date of birth and month of birth (e.g. dd/mm, dd-mm or dd.mm)")
# При неправильном вводе пользователя вывести на экран подсказку корректного вводa


