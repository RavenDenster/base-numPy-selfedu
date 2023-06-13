import numpy as np

a = np.array([1,2,3,4])
print(a)

a = np.array([1, 2, '3', True])
print(a, a[0])
a[1] = 1134
print(a)

print(a[[1,0,1,1,1,1]])

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[True,True,False,False,False,False,False,False,True]])

b = a.reshape(3,3)
print(b, b[2][0], b[2,0])