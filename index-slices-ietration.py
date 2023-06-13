import numpy as np 

a = np.arange(12)
b = a[2:4] # не новый массив, а новое представление массива
# print(b)
b = a[3:]
# print(b)
b = a[:3]
# print(b)
b = a[::-1]
# print(b)

b = a[4::2] = np.array([10,20,30,40])
# print(a)

# for x in a:
#     print(x, sep=' ', end=' ')

a = np.array([(1,2,3), (10,20,30), (100,200,300)])
# print(a[0, :])
# print(a[:, 1])

# for val in a.flat: # предвращает матрицу в векртор, что бы не делать вложенные циклы
#     print(val, end=' ')

a = np.arange(1,82).reshape(3,3,3,3)
# print(a[..., 1, 1])

a = np.arange(9)
a[[0,1,7,5]] = [40,20,10,60] # присваеваем
c = a[[0,0,1,7,5]] # это копия массива (называется списочное индексирование)
# print(c)

indx = [0,0,1,1,1,2]
c = a[indx]
# print(c)
bindx = [True, True, False, False, False, True, False, False, False]
c = a[bindx]
# print(c)

i = a > 5
# print(i)
# print(a[i])
# print(a[a>5])
