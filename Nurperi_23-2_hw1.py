# Написать программу для вычисления среднего показателя температуры воздуха в Кыргызстане на сегодня.
print("The average air temperature in Kyrgyzstan today")

# Температура каждой области должна вводиться пользователем по запросу программы.
Batken = float(input("Enter the temperature of Batken: "))
Jalalabat = float(input("Enter the temperature of Jalalabat: "))
Issykkul = float(input("Enter the temperature of Issykkul: "))
Naryn = float(input("Enter the temperature of Naryn: "))
Osh = float(input("Enter the temperature of Osh: "))
Talas = float(input("Enter the temperature of Talas: "))
Chui = float(input("Enter the temperature of Chui: "))

# Средний показатель должен быть в виде числа с плавающей точкой с одной цифрой после точки (float).
average_temperature = round((Batken + Jalalabat + Issykkul + Naryn + Osh + Talas + Chui)/7, 1)

print("The average air temperature in Kyrgystan today is", average_temperature, "°C")
