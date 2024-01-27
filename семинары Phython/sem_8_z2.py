# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
number = "8 11 0 -23 140 1"
abraFilter = filter(lambda x:10 <= abs(x) <=99, map(int,number.split()))

result = ' '. join(map(str, abraFilter))
print(result)

print(list(filter(lambda x : len(str(abs(int(x)))) ==2, number.split())))