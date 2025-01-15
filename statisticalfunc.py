import numpy as np
import statistics as stats
baked_food = [200,300,150,130,200,280,170,188]
a=np.array(baked_food)

print(np.mean(baked_food)) #sum of all values
print(np.median(baked_food)) #SORT THEN MIDDLE ELEMENT
print(stats.mode(baked_food))
print(np.std(baked_food)) #standard deviation
print(np.var(baked_food)) #variance

