import pandas as pd 
import numpy as np 
import random
#Импортирую библотеки 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
#  
print('')

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)
#
# работа на семинаре
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst, '42':[i for i in lst] })
# data['42'] = data['42'].map({'robot' : 666})
# data = data.drop('42',axis = 1)
# data.head()
