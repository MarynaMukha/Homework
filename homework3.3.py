# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

# создаем список
numbers: list[int] = [1, 2, 3, 4, 5]

# проверяем остаток от деления для поиска парных и непарных значений
if len(numbers) % 2 == 0:
    list1 = numbers[0:len(numbers) // 2]
    list2 = numbers[len(numbers) // 2:]
if len(numbers) % 2 > 0:
    list1 = numbers[0:len(numbers) // 2 + 1]
    list2 = numbers[len(numbers) // 2 + 1:]

result = [list1, list2]
print(result)
