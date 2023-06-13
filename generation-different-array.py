
import numpy as np

empty = np.empty(10) # возвращает новый массив заданного размера и типа данных, но без определенных значений
# print(empty)
empty = np.empty((3,2), dtype='int16')
# print(empty)

eye = np.eye(4) # по главной диагонали нули
# print(eye)
eye = np.eye(4, 2)
# print(eye)

identity = np.identity(5) # возвращает квадр. матрицу с единиц по главной диагонали
# print(identity)

zeros = np.zeros((2,3,4))
# print(zeros)

ones = np.ones([4,3], dtype='int8')
# print(ones)

full = np.full((3,2), -1)
# print(full)

# =================================================================

mat = np.mat('1 2 3 4')
# print(mat)
mat = np.mat('1, 2, 3, 4')
# print(mat)
mat = np.mat('1, 2; 3, 4')
# print(mat)
mat = np.mat([5,4,3])
# print(mat)
mat = np.mat([(1,2,3), (4,5,6)])
# print(mat)

diag = np.diag([1,2,3]) # если одномерный массив, то создаётся матрица
# print(diag)
diag = np.diag([(1,2,3), (4,5,6), (7,8,9)]) # если двухмерный, то он выделяет диагональ
# print(diag)
diagflat = np.diagflat([(1,2,3), (4,5,6), (7,8,9)]) # в отличие от diag создаёт полноценную матрицу
# print(diagflat)

tri = np.tri(4)
# print(tri)
a = np.array([(1,2,3), (4,5,6), (7,8,9)])
tri = np.tril(a)
# print(tri)
triu = np.triu(a)
# print(triu)
vander = np.vander([1,2,3])
# print(vander)


arange = np.arange(5)
# print(arange)
arange = np.arange(1, 5)
# print(arange)
arange = np.arange(1, 5, 0.5)
# print(arange)
arange = np.arange(0, np.pi, 0.1)
# print(arange)
cos = np.cos(np.arange(0, np.pi, 0.1))
# print(cos)

linspace = np.linspace(0, np.pi, 3)
# print(linspace)
log = np.logspace(0, 1, 3)
# print(log)
geomspace = np.geomspace(1,16,5) # начальное, конечное значение, кол-во
# print(geomspace)

# =======================================================

a = np.array([(1,2), (4,5)])
b = np.copy(a)
# print(b)
# print(np.fromfunction(lambda x,y: x*100 + y, (2,2))) # x, y - index
fromiter = np.fromiter('hello', dtype='U1') # создаём на основе любого итерируемого объекта
fromsting = np.fromstring('1 2 3', dtype='int16', sep=' ')
# print(fromsting)
fromsting = np.fromstring('1, 2, 3', dtype='int16', sep=',')
# print(fromsting)