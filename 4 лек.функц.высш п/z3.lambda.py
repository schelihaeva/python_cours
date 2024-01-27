def calk1(a,b):
    return a+b

def math (op, x,y): #передаем значения в функцию с оператором x
      print(op(x,y))
# calk1 = lambda a,b: a+b #   указываем, что calk1- это lambda функция, котороая должна a+b

math(lambda a,b: a+b,5,45)