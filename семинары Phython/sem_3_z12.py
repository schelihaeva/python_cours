# обращение к словарям, 3 способа

di = {'dd':12, (1,2):'dd', 125:[1,2,88]}




print(di)
for i in di:
    print(di[i],  end = '  ')
print()
    
print(di)

#2 cпособ
for i in di.values():
    print(i,  end = '  ')
print()
print()
# 3 способ
for i,j in di.items():
    print(j ,  end = '  ')