# Вывести на экран календарь введенного пользователем месяца и года

import calendar

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))
