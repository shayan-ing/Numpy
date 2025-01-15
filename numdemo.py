import numpy as np


a = np.array([10,20,30])
b = np.array([40,50,60])

print(a)
print(b)
print(a+b)


import numpy as np

arr = np.array([[10,20,30,40],[50,60,70,80]])

# print(arr[0:3,0:3])

print(np.shape(arr))

print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)