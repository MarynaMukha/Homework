# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

# создаем список
numbers: list[int] = [0, 1, 0, 12, 3]

for i in range(numbers.count(0)):
        # извлекаем позицию по первому вхождению
        position =  numbers.index(0)
        # переносим 0 в конец списка
        numbers.insert(len(numbers), numbers[position])
        # удаляем перенесенный элемент
        numbers.pop(position)
# выводим последний результат цикла
if i == numbers.count(0) - 1:
        print("New list: ", numbers)
