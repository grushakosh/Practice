# Вводится целое положительное число n. 
# Вычислить и вывести на экран сумму: 1 + 1/2 + 1/3 + ... + 1/n с точностью до тысячных (три знака после запятой). 
# Программу реализовать при помощи цикла while.


n = int(input())

i = 1
res = 0

while i <= n:
    res += 1/i
    i+=1
    
print(round(res, 3))
