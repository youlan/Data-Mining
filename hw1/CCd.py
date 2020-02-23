import numpy as np
import matplotlib.pyplot as plt
import time
import random




mlist = [400, 2000, 5000]
nlist = np.linspace(100, 20000, 5, dtype="I")
#mlist = [400]
#nlist = [300]
timelist = np.zeros((5, 3))

for ml in range(len(mlist)):
    m = mlist[ml]
    for s in range(len(nlist)):
        n = nlist[s]
        start = time.time()
        for r in range(m):
            dlist = set()
            while len(dlist) < n-1:
                sample = random.randint(0, n-1)
                #k += 1
                if sample not in dlist:
                    dlist.add(sample)
        end = time.time()
        runtime = end-start
        print(m, n, runtime)
        timelist[s, ml] = runtime

#np.savetxt("CCd.csv", timelist, delimiter=",")


for ml in range(len(mlist)):
    plt.plot(nlist, timelist[:, ml], marker="*", label="m = "+str(mlist[ml]))
plt.title("Coupon Collectors")
plt.xlabel("n")
plt.ylabel("time (s)")
plt.legend(loc="upper left")
plt.show()
plt.savefig("CCd.png")