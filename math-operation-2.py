import numpy as np

a = np.array([1,2,3,10,20,30])
# print(a.sum())
# print(a.mean()) # среднее арифм
# print(a.max())
# print(a.min())

a.resize(3, 2)
# print(a.sum(axis=0))

a = np.array([-1, 1, 5, -44, 32, 2])
# print(np.abs(a))
# print(np.amax(a))
# print(np.amin(a))
# print(np.round(a))
# print(np.argmax(a))
# print(np.argmin(a))

a.resize(2,3)
# print(np.amax(a, axis=0))

a = np.linspace(0, np.pi, 10)
# print(np.sin(a))
# print(np.cos(a))

# print(np.random.rand())
# print(np.random.rand(5))
# print(np.random.randint(5, 10)) # целые числа от 5 до 10
# print(np.random.randint(5, size=4))
# print(np.random.randn()) # по гауссовскому закону распределения (c нулевым мат ожиданием и единичной дисперсией)

# np.rnadom.seed(13) - для сохранения значения получених ранее рандомно

a = np.arange(10)
np.random.shuffle(a) # перитасовка
# print(a)

a = np.random.permutation(10) # работает без предварительного создания массива
# print(a)

