# создание калькулятора
while True:
    # создание переменных для ввода данных с клавиатуры
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
        # запускаем ввод до тех пор пока не будет выбрано корректное математическое действие
    while True:
        action = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nSelect your choice: "))
        if 0 < action <= 4:
            break
        else:
            print("Invalid action please try again")
    if action == 1:
        print("Result: ", number1 + number2)
    if action == 2:
        print("Result: ", number1 - number2)
    if action == 3:
        print("Result: ",number1 * number2)
    if action == 4:
        if number2 == 0:
            print("Invalid second number try again")
        else:
            print("Result: ", float(number1 / number2))
    # останавливаем программу только при вводе N и продолжаем при - Y, что бы минимизировать ошибку ввода
    while True:
        final_action = (input("Continue (Y/N)?: "))
        if final_action == "Y":
            break
        elif final_action == "N":
            exit()
        else:
            print("Invalid action please try again")





