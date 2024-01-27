# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
# print(‘same’) else:
# print(‘different’)
values = [4, 2, 10, 6]

def same_by(characteristic, objects):
    filter_lst = list(filter(characteristic, objects))
    return len(objects) == len(filter_lst)

if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")
