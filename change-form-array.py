import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8,9])
a.shape = -1, 2
# print(a)

c = a.ravel() # выдягивает матрицу в обычный вектор
# print(c)

a.resize(10, 1) # измениться сам массив
# print(a)
a.resize(3,3,refcheck=False)
# print(a)
a.resize(4,5,refcheck=False)
# print(a)

a = np.array([(1,2,3), (1,4,9), (1,8,27)])
# print(a)
b = a.T # транспорирование (меняем оси местами)
# print(b)

x_test = np.arange(32).reshape(8,2,2)
# print(x_test)
x_test4 = np.expand_dims(x_test, axis=0) # создаёт лишь представление
# print(x_test4.shape) # в одном элементе находится трёх мерная матрица

a = np.append(x_test4, x_test4, axis=0)
# print(a.shape)
b = np.delete(a, 0, axis=0)
# print(b.shape)
b = np.expand_dims(x_test4, axis=-1)
# print(b.shape)

c = np.squeeze(b) # удаляет оси длиной в один элемент
# print(c.shape)

a = np.arange(1, 10)
b = a[np.newaxis, :, np.newaxis] # добавляем ось, а все остальные элементы остаются
# print(b.shape)