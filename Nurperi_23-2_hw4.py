print('Tuple of Letters and Numbers')
# Дан кортеж состоящий из разных типов данных:
data_tuple = ('h', 6.13,  'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

# 1) Создать два пустых списка letters и numbers
letters = []
numbers = []

# 2) Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
         numbers.append(i)

# 3) Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
numbers.remove(6.13)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(1, 2)

# 4) Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
numbers.sort()
letters.reverse()
letters[1] = 'g'.upper()
letters[7] = 'c'.lower()

# 5) Измените список numbers в список квадратов своих же чисел
squared_numbers = []
for number in numbers:
    squared_numbers.append(number**2)

# 6) Преобразовать списки numbers и letters в кортежи
letters = tuple(letters)
numbers = tuple(squared_numbers)

print(letters)
print(numbers)
