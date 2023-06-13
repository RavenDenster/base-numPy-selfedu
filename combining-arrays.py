import numpy as np

a = np.array([(1,2), (3,4)])
b = np.array([(5,6), (7,8)])

hstack = np.hstack([a,b]) # объединение по горизонтали
vstack = np.vstack([a,b])# объединение по вертикали
# print(hstack, vstack)

a = np.fromiter(range(18), dtype='int32')
b = np.fromiter(range(18, 36), dtype='int32')
a.resize(3,3,2)
b.resize(3,3,2)
# print(a, b)
c = np.hstack([a,b])
# print(c.shape) # объединяет только по одной оси

a = np.array([1.,2.,3.,4.])
b = np.array([1.,2.,3.,4.])
c = np.column_stack([a,b])
# print(c)
c = np.row_stack([a,b])
# print(c)

a = np.arange(1, 13) 
b = np.arange(13, 26)
a.resize(3,3,2)
b.resize(3,3,2)

c0 = np.concatenate([a,b], axis=0)
c1 = np.concatenate([a,b], axis=1)
c2 = np.concatenate([a,b], axis=2)
# print(c0.shape, c1.shape, c2.shape) # объединение по определённой оси

a = np.r_[[1,2,3],4,5]
b = np.r_[1:9,90,100] # объединение по axis = 0 (верктор строка)
# print(a, b)

a = np.c_[1:5] # объединение по axis = 1 (верктор столбец)
# print(a)

a = np.arange(10)
c = np.hsplit(a, 2)
# print(c)
a.shape = 10, -1
# print(a)
c = np.vsplit(a, 2)
# print(c)
a = np.arange(10)
c = np.array_split(a, 2, axis=0)
# print(c)