#создание переменной для ввода данных с клавиатуры
number = int(input("Enter a five digit number: "))

#извлечение цифр введенного числа
n1 = number // 10000
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number // 10 % 10
n5 = number % 10

#используем конкатенацию для создания обратной последовательности
reverse_num = int(str(n5)+str(n4)+str(n3)+str(n2)+str(n1))

print(reverse_num)

