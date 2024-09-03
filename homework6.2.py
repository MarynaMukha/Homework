# вводим число для расчета даты
number = int(input("Enter a number: "))

if number >= 8640000 or number < 0:
    print("Incorrect number, please try again")
    exit()

# вычитаем количество полных дней/часов/минут/секунд, переводим результат в str что бы
# потом применить функцию zfill и индексацию

days = str(number // (24 * 60 * 60))
hours = str((number - (int(days) * 24 * 60 * 60)) // (60 * 60))
minutes = str((number - (int(days)  * 24 * 60 * 60) - (int(hours) * 60 * 60) ) // 60)
seconds = str(number - (int(days)  * 24 * 60 * 60) - (int(hours) * 60 * 60)  - (int(minutes) * 60))

if days[-1]  == "1" and days != "11":
    print(days, " день, ", hours.zfill(2), ":", minutes.zfill(2), ":", seconds.zfill(2), sep='')
if days[-1]  in ("2", "3","4") and days not in ("12", "13", "14"):
    print(days, " дні, ", hours.zfill(2), ":", minutes.zfill(2), ":", seconds.zfill(2), sep='')
if days[-1] in ("5", "6", "7", "8", "9", "0") or days in ("11", "12", "13", "14"):
    print(days, " днів, ", hours.zfill(2), ":", minutes.zfill(2), ":", seconds.zfill(2), sep='')

