# Вводится шестизначное число. Определить, является ли оно счастливым. 
# (Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.). 
# Вывести ДА, если счастливое и НЕТ - в противном случае.


number = input()

if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
    print('ДА')
else:
    print('НЕТ')