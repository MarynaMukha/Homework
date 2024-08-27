# [1, 3, 5] => 30
# [6] => 36
# [] => 0
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

# создаем список
numbers: list[int] = [0, 1, 7, 2, 4, 8]

i = 0
sum_element = 0

while True:
        if i < len(numbers):
                if i % 2 == 0:
                        element = numbers[i]
                        sum_element = element + sum_element
                        i = i + 1


                else:
                        i = i + 1
                continue

        else:
                break
last_element = numbers[-1]
print("Result: ", last_element * sum_element)



