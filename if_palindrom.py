# Вводится слово. Необходимо определить, является ли это слово палиндромом (одинаково читается вперед и назад, например, АННА). 
# Регистр букв не учитывать. Если введенное слово палиндром, на экран вывести ДА, иначе - НЕТ.


word = input()

if word.lower() == word[::-1].lower():
    print('ДА')
else:
    print('НЕТ')
