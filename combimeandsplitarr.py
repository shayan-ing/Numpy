import numpy as np

a1= np.array([30,40,50])

a2 = np.array([5,5,3])

print(np.concatenate([a1,a2]))

print(np.hstack([a1,a2])) #horizontal concatenation
print(np.vstack([a1,a2])) #vertical concatenation

print(np.append(a1,60))
print(np.insert(a1,1,60)) #array,index,value
print(np.delete(a1,[30])) 