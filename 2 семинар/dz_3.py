# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
N = abs(int(input('Введите число N ')))
stop = 0
k = 2
for i in range(N):
    if stop != 1:
        k = k ** i
        if k <= N:
            print(k, end=' ')
            k = 2
        else:
            stop = 1
    else:
        i = N