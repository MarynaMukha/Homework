# создание переменных для ввода данных с клавиатуры
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
action = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nSelect your choice: "))

# создание калькулятора
match action:
    case 1:
        print("Result: ",number1 + number2)
    case 2:
        print("Result: ",number1 - number2)
    case 3:
        print("Result: ",number1 * number2)
    case 4 if number2 != 0:
        print("Result: ",float(number1 / number2))
    case _:
        print("Invalid input please try again")