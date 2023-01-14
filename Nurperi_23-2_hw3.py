# Счетчик гласных и согласных букв
print("Vowel and consonant letter counter".title())

# Считывать строчные и прописные буквы
vowels = "AEIOUaeiouАЫЕИОУЭаыеиоуэ"
consonants = "QWERTYUIOPASDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnmЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮйцкнгшщзхфвпрлджэячсмтбюъь"

count_vowels = 0
count_consonants = 0
# Программа должна работать в бесконечном цикле с возможностью выхода
# Запрашивать у пользователя любое слово на латинице или кириллице
while True:
    word = input("Enter the word [Type '1' to quit] / Введите слово [Введите '1' чтобы выйти]: ")
    if word == "1":
        break
    print("Number of letters/Количество букв:", len(word))  # Вывести общее количество букв в данном слове
    for i in word:
        if i in vowels:
            count_vowels += 1
        if i in consonants:
            count_consonants += 1

# Вывести количество согласных и гласных букв
    print("Vowels/Гласные:", str(count_vowels))
    print("Сonsonants/Согласные:", str(count_consonants))

# Вывести процентное соотношение гласных и согласных букв до двух цифр после точки
    persentage_c = float((count_consonants / (count_consonants + count_vowels)) * 100)
    persentage_v = float((count_vowels / (count_vowels + count_consonants)) * 100)
    print("Vowels/Consonants / Гласные/Согласные:", round(persentage_v, 2), "%", "/", round(persentage_c, 2), "%")
