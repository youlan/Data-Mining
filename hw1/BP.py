
import numpy as np
import matplotlib.pyplot as plt
import time

def sample_function(n):
    k = 1
    nlist = []
    t = 0
    random = np.random.randint(low=0, high=n, size=1)
    while t == 0:
        if random in nlist:
            return k
        else:
            nlist.append(random)
            k += 1
            random = np.random.randint(low=0, high=n, size=1)

timelist = np.zeros((10, 3))
mlist = [300, 5000, 10000]
nlist = np.arange(100, 1000000, 10)
klist=[]
for ml in range(len(mlist)):
    m = mlist[ml]
    print(m)
    for z in range(len(nlist)):
        n = nlist[z]
        print(n)
        start = time.time()
        for j in range(m):
            k = sample_function(n)
            #klist.append(k)
        end = time.time()
        timelist[z, ml] = end - start

#mean = np.sum(klist)/300
#print(mean)
#np.savetxt("BPd.csv", timelist, delimiter=",")


for s in range(len(mlist)):
    plt.scatter(nlist, timelist[:,s], marker="*", label="m = "+str(mlist[s]))
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

