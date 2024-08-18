#создание переменной для ввода данных с клавиатуры
number = int(input("Enter a four digit number: "))

#извлечение цифр введенного числа
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10

#вывод результата
print(n1)
print(n2)
print(n3)
print(n4)