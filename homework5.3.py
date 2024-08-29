# вводим строку
initial_str = input("Enter initial string: ")

import string

punctuation = string.punctuation
result = ""

for letter in initial_str:
        if punctuation.count(letter) > 0:
            result = result
        else: result = result + letter

# убираем пробелы, заменяем на большой регистр первую букву каждого слова
upper_str = result.title().replace(" ", "")

# добавляем # к началу новой строки
new_str = "#" + upper_str

# обрезаем длину до 140
print(new_str [:140])



