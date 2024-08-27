import random

# вводим длину списка
size = int(input("Enter the length of the list: "))

# создаем рандомный список
numbers = []
for i in range(size):
    numbers.append(random.randint(3, 10))
print(numbers)

# выводим 1, 3 и второй с конца элемент
if len(numbers) < 3:
    print("Invalid value was added")
else:
    num_1 = numbers[0]
    num_2 = numbers[2]
    num_3 = numbers[-2]

    result = [num_1, num_2, num_3]
    print(result)





