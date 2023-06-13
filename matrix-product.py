import numpy as np

a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
# print(np.dot(a, b))
# print(np.matmul(a, b))

a = np.arange(1, 10)
b = np.ones(9)
# print(np.dot(a,b))
# print(np.inner(a,b))
# print(np.outer(a,b))
# print(a @ b) # внутренне умножение двух векторов

a = np.array([1,2,3])
b = np.arange(4,10).reshape(3,2)
print(np.dot(a, b)) # векртор умножается на первый столбец, а потом на второй