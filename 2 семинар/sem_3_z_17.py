# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

list = [1, 1, 2, 0, -1, 3, 4, 4]
print(list)
print(f'В заданном списке {len(set(list))} различных чисел') # set - срез, таким образом покащывает кол-во элементов в списке

# 2 вариант решения (пользователь вводит значения самостоятельно)

# list_1 = []            # создали пустой список
# n = int(input('Введите количество элементов в списке '))          
# for i in range(n):     # цикл выполнится n раз
#     i = int(input('Введите элемент списка ')) # пользователь вводит элементы списка
#     list_1.append(i)
# print(list_1)
# another_set=set(list_1)
# print(f'В заданном списке {len(another_set)} различных чисел')


# решение на семинаре

list = [1, 1, 2, 0, -1, 3, 4, 4]
temp = set(list)
x = set()
print(x)

print(temp)
print(len(temp))

list2 = []
list2.append(list[0])
print(list2)

for i in list:
    if i in list2:
        list2.append(i)

print(list2)

