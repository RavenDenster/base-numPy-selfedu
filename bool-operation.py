import numpy  as np

a = np.array([1,2,3,10,20,30])
b = np.array([1,2,3,4,5,6])
print(a == b)
print(a != b)

print(np.greater(a, b)) # a > b
print(np.less(a, b)) # a < b
print(np.equal(a, b)) # a == b

if np.array_equal(a, b):
    print('a == b')

print(np.any(a > 5)) # хотя бы один элемент больше 5
print(np.all(a > 5)) # все элементы больше 5


a = np.array([1, 2, np.nan, np.inf, -np.inf])
print(np.isinf(a))
print(np.isnan(a))

indx = np.isinf(a)
print(a[~indx]) # ~ это инверсия

print(np.isfinite(a)) # только числовые значения

# np.iscomplex, np.isreal - для нахождения комплексных, для находжения действительных чисел

X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])

print(np.logical_and(X,Y))
print(np.logical_or(X,Y))
print(np.logical_not(X))
print(np.logical_xor(X,Y))