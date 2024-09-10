def add_one(some_list: list[int]):
    string = ""
    for i in some_list:
        string += str(i)
    number = int(string)+1
    final_list = []
    for j in str(number):
        final_list.append(int(j))
    return final_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")