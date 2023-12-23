# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# N = abs(int(input('Введите число N ')))
# stop = 0
# k = 2 # возводим 2 в  степень
# for i in range(N):  # создание списка чисел
#     if stop != 1: # если stop не равно 1
#         k = k ** i # тогда k возводим в степень i
#         if k <= N: # при k <= N
#             print(k, end=' ') # выводим k
#             k = 2
#         else:
#             stop = 1
#     else:
#         i = N

def powers_of_two(n):
    power = 0
    result = 1

    while result <= n:
        print(result)
        power += 1
        result = 2 ** power

powers_of_two(n)