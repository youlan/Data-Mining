
import numpy as np
import matplotlib.pyplot as plt
import time
import random

def sample_function(n):
    k = 1
    nlist = set()
    t = 0
    r = random.randint(1, n)
    while t == 0:
        if r in nlist:
            return k
        else:
            nlist.add(r)
            k += 1
            r = random.randint(1, n)

timelist = np.zeros((10, 3))
mlist = [300, 5000, 10000]
nlist = np.linspace(100, 1000000, 10, dtype="I")
#nlist = [300, 500]
#mlist = [300]
#nlist = [5000]
print(nlist)
klist=[]
for ml in range(len(mlist)):
    m = mlist[ml]
    print(m)
    for z in range(len(nlist)):
        #print(z)
        n = nlist[z]
        print(n)
        start = time.time()
        for j in range(m):
            k = sample_function(n)
        end = time.time()
        print(end-start)
        timelist[z, ml] = end - start
np.savetxt("BPd.csv", timelist, delimiter=",")
#mean = np.sum(klist)/300
#print(mean)
#np.savetxt("BPd.csv", timelist, delimiter=",")
#print(timelist)

for s in range(len(mlist)):
    plt.plot(nlist, timelist[:,s], marker="*", label="m = "+str(mlist[s]))
plt.title("Birthday Paradox")
plt.xlabel("n")
plt.ylabel("time (s)")
plt.legend(loc="upper left")
plt.show()
'''

X = range(0, 300)
Y = []
for i in range(len(X)):
    y_val = 0
    for k in range(len(klist)):
        if klist[k] <= X[i]:
            y_val += 1
    #print(y_val)
    Y.append(y_val/300)

mean = np.sum(klist)/300
print(mean)

plt.scatter(X, Y, marker="*")
plt.title("Birthday Paradox CDP")
plt.xlabel("Trails of k")
plt.ylabel("Probability of success")
plt.show()
'''

