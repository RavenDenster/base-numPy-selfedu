import numpy as np

a = np.array([1,2,3,4], 'float64')
print(a)
# print(np.sctypeDict) все типы данных (bool, int, intc, intp, int8, int16, int32, int64, uint,8,uint16,uint32,uint64,float,float16,float32,float64,complex,complex64,complex128,str)
print(np.int16(10.5))

b = np.complex64(a)
print(b)

c = np.array((1,2,3))
print(c)
d = np.array("Hello")
print(d)