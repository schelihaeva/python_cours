# 1 способ
#n = 100

#res =print(n//100 + n//10%10 + n%10)

 # 2 способ
n = input("Введите трехзначное число: ")
n = int(n)
 
d1 = n % 10
d2 = n // 100
d3 = n // 10%10
 
print("Сумма цифр числа:", d1 + d2 + d3)