import numpy as np

lst = [1,2,3]
a = np.array([1,2,3])
print(lst * 2)
print(a * 2)
print(-a)
print(a - 3)
print(a + 2)
print(a / 5)
print(a // 2)
print(a ** 3)
print(a % 2)

b = np.array([3,4,5])
print(a-b)

b += 5
print(b)