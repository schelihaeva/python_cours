#найти факториал числа через рекурсию

def fac(n):
    if n == 1: # == двойное равенство
        return 1# возвращаем 1
    return fac(n - 1) * n # вызываем функцию, перемножаем переменные
 
 
print(fac(6))