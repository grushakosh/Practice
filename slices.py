#  Напишите программу отображения всех символов с нечетными индексами из введенной строки.


s = input()
print(s[1::2])


# Имеется список с оценками студента:
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# Необходимо с помощью срезов выбрать элементы через один, начиная с последнего, и вывести результат на экран.


m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-2])
