
# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
#list = list[-k:] + list[:-steps] т.е. сделать срез списка
# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k):
#     t=list[0]
#     for i in range(len(list)-1):
#         list[i]=list[i+1]
#     list[-1]=t
# print(list)
        
# # 2 вариант 

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k-1):
#     tmp = list[-1]
#     list.insert(0, tmp)
#     list.pop()
# print(list)

# 3 вариант решения задачи

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k-1):
#     list.insert(0, list.pop()) # list.pop - извлекает последний элемент, 
# print(list) 
#                    # list.insert(0, - ставит его на нулевую позицию
#print(list.pop()) # list.pop - возвращает последний элемент
# работа на семинаре
list = [1, 2, 3, 4, 5]
k = 33
k = k % len(list)

list2 = [0] * len(list)

for i in range(len(list)):
    if i + k < len(list):
        list2[i+k] = list[i]
        print(list2)
    else:
        list2[i+k-len(list)] = list[i-len(list)]
        print(list2)
for i in range(k):
    temp = list.pop(k)

print(list.pop())
print(list.remove(3))
print(list)