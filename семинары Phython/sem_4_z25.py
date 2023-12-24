# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# lst = 'a a a b c a a d c d d'
# print(lst)
# lst = 'a a a b c + + a       a +d +c       d d'.replace('+'," ").split()
# print(lst)
# str = 'a a a b c a a d c d d'
# list_1 = str.split()
# print(str)
# result = list()

# for i in list_1:
#     count = 0
#     if i in result:
#         for j in result:
#             if i == j[0]:
#                 count += 1
#         result.append(f"{i}_{count}")
#     else:
#         result.append(i)

# print(" ".join(result))
str = 'a a a b c a a d c d d'
list_1 = str.split()
print(str)
result = list()

for i in list_1:
    count = 0
    if i in result:
        for j in result:
            if i == j[0]:
                count += 1
        result.append(f"{i}_{count}")
    else:
        result.append(i)

print(" ".join(result))