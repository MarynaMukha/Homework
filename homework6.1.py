# вводим промежуток алфавита
range_data = input("Enter the range: ")

# ищем первую и последнюю букву промежутка
letter1 = range_data[0]
letter2 = range_data[-1]

# выводим сообщение если введено что-то кроме букв
if not letter1.isalpha() or not letter2.isalpha():
    print("Incorrect, only letters are allowed")

import string
alphabet = string.ascii_letters

# ищем индексы первой и последней буквы в string.ascii_letters
range1 = alphabet.find(letter1)
range2 = alphabet.find(letter2) + 1

print(alphabet[range1:range2])

