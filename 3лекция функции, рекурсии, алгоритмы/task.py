# Функция — это фрагмент программы, используемый многократно
# Мы знакомы уже с функциями с C#, давайте теперь посмотрим, как создаются и используются функции внутри Python.
# def function_name(x):
# # body line 1
# # ...
# # body line n
# # optional return
# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.
def sumNumbers(n):
 summa = 0
 for i in range(1, n + 1): # задаем цикл range ,чтобы считало с 1, ставим в (1, n+1)
                summa +=i  # сумму будем увеличивать на 1, но чтобы ее увеличивать, ее надо создать, создаем в стр 10   
                print(summa) # выводим функцию
sumNumbers(5)        # вызываем функцию, пишем ее имя, в параметрах () указываем число        