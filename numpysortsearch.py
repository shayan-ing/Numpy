import numpy as np

# ar = np.array([[7,8,4,12,9],[2,8,5,1,3]])

# print(np.sort(ar))

ar=np.array([3,4,1,2,7])

# s=np.where(ar==4)
# s=np.where(ar%2==0)
# print(s)

ss=np.searchsorted(ar,2)
print(ss)