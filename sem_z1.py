#Задача No1. Решение в группах
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700 m = 750 Output: 2
# мой способ
n = 700 # проезжает в день км
m = 750 # проехала всего км
#print((m+n-1)//n)
print(abs (m//n)) # abs переводит в целочисленное