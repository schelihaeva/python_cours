list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))# list1 =равен другому списку , к каждому значению +10, выводим список list, в функцию map передаем 2 значения
print(list_1)