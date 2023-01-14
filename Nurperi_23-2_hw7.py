# Расширить функцию “Ближайшее Число” из ДЗ № 6
# На этот раз Функция должна вернуть искомое число и отсортированный список в порядке приближенности к указанному числу.
# Всё это должно быть в кортеже.

def nearest_number(list, number = float(19)):
    return number, sorted(list, key=lambda x: abs(number-x))
# Тест:
print('1-задание:', nearest_number([30,11,15,9,190,16,1], 27))

# Напишите примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение.
example_with_filter = [34, 304, 67, 115, 164, 72, 288]
filtered = tuple(filter(lambda x: x%4==0, example_with_filter))
print('3-задание, filtered:', filtered)

example_with_map = [34, 304, 67, 115, 164, 72, 288]
mapped = tuple(map(lambda x: x-34, example_with_map))
print('3-задание, mapped:', mapped)

# Создать функцию для вывода элемента списка/кортежа/строки (iterable) по указанному индексу.
output_elem = lambda iter, ind: iter[ind]

example = 12, 'string', 1.5, False

while True:  # Функция должна работать в бесконечном цикле с командой выхода.
    try:
        index = int(input('2-задание, введите индекс: '))  # Индекс должен запрашиваться программой при запуске.
        if index == 999:
            break
        print(output_elem(example, index))
    except:
        print('Please, enter actual indexes!')      # При неверно указанном индексе использовать исключения
                                                    # с подсказкой ввода актуальных индексов указанного списка.
