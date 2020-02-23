import numpy as np
import matplotlib.pyplot as plt
import time



klist = np.zeros(400)
start = time.time()
for r in range(399):
    k = 0
    nlist = np.arange(300).tolist()
    while len(nlist):
        s = np.random.randint(low=0, high=300, size=1, dtype="I")
        k += 1
        if s in nlist:
            nlist.remove(s)
    klist[r] = k
    #print(k)
    r += 1
end = time.time()
print(end-start)



X = range(4000)
Y = []
for i in range(len(X)):
    y_val = 0
    for k in range(len(klist)):
        if klist[k] <= X[i]:
            y_val += 1
    #print(y_val)
    Y.append(y_val/400)

mean = np.sum(klist)/400
print(mean)

plt.scatter(X, Y, marker="*")
plt.title("Coupon Collectors CDP")
plt.xlabel("Trails of k")
plt.ylabel("Probability of success")
plt.show()