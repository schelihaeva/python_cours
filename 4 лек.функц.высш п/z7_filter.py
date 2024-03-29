
# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True.
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data)) #filter работает с данными, кторые задаем
print(res) # [0, 2, 4, 6, 8]

