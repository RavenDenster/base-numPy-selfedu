import numpy as np

a = np.array([1,2,3,4,4,3,2,1])
setA = np.unique(a)
# print(setA)

setA = np.unique(a, return_counts=True) # количество повторений
# print(setA)
 
setA = np.unique(a, return_index=True) # на каком индексе появилось число
# print(setA)

setA, indx = np.unique(a, return_inverse=True) # создаёт массив с индесами
# print(setA[indx])

x = np.array([[0,1,1,2],[0,1,1,2],[9,1,1,2]])
setX = np.unique(x, axis=1)
# print(setX)

x = np.array([0,1,2,3])
y = np.array([1,2,3,4,5,6,7,8])
a = np.in1d(x,y)
print(a)

a = np.intersect1d(x,y) # определяет пересечения
print(a)

a = np.union1d(x,y) # объединение
print(a)

a = np.setdiff1d(x, y) # вычитание
print(a)

a = np.setxor1d(x,y) # не общие элементы
print(a)