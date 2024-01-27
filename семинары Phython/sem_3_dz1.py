# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5, 3, 3] 
# print(list_1)
# k= int(input("Введите элемент из списка"))
# conunt = list_1.count('Количество элементов в списке: ')
# print(conunt)

# 2 cпособ
# list_1 = [1, 2, 3, 2, 4, 1, 5, 2]
# k = [2]
# for item in list_1:
#     if list_1.count(item) > 1 and item not in k:
#         k.append(item)

# print("Повторяющиеся элементы в списке:", k)

# list_1 = [1, 2, 3, 2, 4, 1, 5, 2, 1]
# k = count(list_1)
# for item, count in k.items():
#     if count > 1:
#         print(f"Элемент {item} повторяется {count} раз(а).")

        # 
list_1 = [1, 2, 3, 4, 5, 3, 3]    
k = 5  #вводим число из списка
count_k = 0

for temp in list_1: # задаем цикл
    if temp == k: # условие если temp==k
        count_k += 1 #если условие не выполнено, то увеличиваем на 1

print(count_k)

# 2 способ
print(list_1.count(k))