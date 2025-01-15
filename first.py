import datetime

x=datetime.datetime.now()
print(x)

y = datetime.datetime(2005,3,20)
print(y)

print(y.strftime("%A"))

import demo01 as d

a = d.add(2,3)

print(a)