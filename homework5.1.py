# вводим строку
initial_str = input("Enter variables name: ")

import string
import keyword

punctuation = string.punctuation
kwlist = keyword.kwlist

# перебираем знаки пунктуации и выводим результат если значение не "_"
result = ""
for letter in punctuation:
    if letter != "_":
        result = result + letter

while True:
    final_action = True
    # проверяем наличие знаков пунктуации
    for symbol in result:
        if initial_str.count(symbol) > 0:
            final_action = False
            break

    # проверка в списке зарегистрированных слов
    if initial_str in kwlist:
        final_action = False

    # проверка на наличие пробелов
    if initial_str.count(" ") > 0:
        final_action = False

    # проверка на то что первый символ не цифра
    if initial_str[0].isdigit():
        final_action = False

    # проверка на наличие большого регистра в строке
    for upper in initial_str:
        if upper.isupper():
            final_action = False
            break

    # проверка на количество "_"
    if not initial_str.upper().isupper() and initial_str.count("_") > 1:
        final_action = False

    print(final_action)
    break








