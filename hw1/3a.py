import numpy as np

n = 5000
p = 1

for i in range(100):
    print(i)
    sp = (5000-i)/5000
    p = p * sp
    print(p)
    if 1 - p > 0.5:
        break

k = 300*(0.577 + np.log(300))
print(k)