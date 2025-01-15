import numpy as np

a = np.array([20,30,40,50])

print(np.sum(a))

print(np.min(a))
print(np.max(a))

print(np.size(a))
print(np.mean(a))

print(np.cumsum(a)) #cumulative sum
print(np.cumprod(a)) #cumualtive product

a = [100,150,199,200,250,130]
b = [10,50,30,40,30,10]

price = np.array(a)
quantity=np.array(b)

print(price,"\n",quantity)

# print(np.cumsum([price,quantity]))
c=(np.cumprod([price,quantity],axis=0))
print(c)

print(c[1].sum())