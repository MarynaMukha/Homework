def common_elements():
    # создаем первый список с шагом 3
    list1 = []
    for i in range (0,100,3):
        list1.append(i)

    # создаем второй список с шагом 5
    list2 = []
    for i in range (0,100,5):
        list2.append(i)

    # переобразовываем list в set
    set_list1 = set(list1)
    set_list2 = set(list2)

    # возвращаем пересечения
    return set_list1&set_list2

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'test1'
print("OK")