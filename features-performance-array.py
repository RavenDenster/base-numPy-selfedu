import numpy as np

a = np.array([0.1, 0.2, 0.3])
a.dtype = np.int8()
print(a, a.size)
print(a.itemsize) # сколько байт занимет один элемент

b = np.ones((3,4,5))
print(b.ndim) # колитчество осей
print(b.shape) # количество элементов по каждой оси
b.shape = 12, 5
print(b)
c = b.reshape(3,2,10) # она не создаёт нового массива, а создаёт другое представление тех же данных
print(c)
d = b.T # трансопинование
print(d)
# массивы и их представления это разные понятия

a = np.array([1,2,3,4,5,6,7,8,9])
b = a.view() # копия представления
a.shape = 3,3 
print(b)

a = np.array([1,2,3,4,5,6,7,8,9])
b = a.copy() # копия данных массива