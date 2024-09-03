# вводим число
number = int(input("Enter a number: "))

while number > 9:
    new_number = 1
    for digit in str(number):
        new_number = new_number * int(digit)
    number = new_number

print(number)