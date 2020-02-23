import numpy as np
import matplotlib.pyplot as plt
import time


nlist = np.arange(300).tolist()
k = 0
while len(nlist):
    s = np.random.randint(low=0, high=300, size=1, dtype="I")
    k += 1
    if s in nlist:
        nlist.remove(s)
print(k)
