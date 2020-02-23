import hashlib, sys
import random, string
import time
import numpy as np
import matplotlib.pyplot as plt

def hashfun(doc, salt):
    hash = hashlib.sha1()
    hash.update(salt.encode("utf-8"))
    hash.update(doc.encode("utf-8"))
    return hash.hexdigest()

f1 = open("D1.txt", "r")
f2 = open("D2.txt", "r")
string1 = f1.readlines()
string2 = f2.readlines()
f1.close()
f2.close()

out1_2 = [(string1[0][j:j + 3]) for j in range(0, len(string1[0])-2)]
out1_2 = sorted(set(out1_2))
out2_2 = [(string2[0][j:j + 3]) for j in range(0, len(string2[0])-2)]
out2_2 = sorted(set(out2_2))

T = [20, 60, 150, 300, 600]
#T = [20,60]
JS = np.zeros((100, 5))
runTime = np.zeros((100,5))


for r in range(len(T)):
    t = T[r]
    print(t)
    for k in range(100):

        start = time.time()
        m1 = {}
        m2 = {}
        salt = []
        simiValue = 0
        for i in range(1, t):
            ran_st = ''.join(random.sample(string.ascii_letters + string.digits, 5))
           #print(ran_st)
            for ele in out1_2:
                temp = hashfun(ele, ran_st)
                if i not in m1 or temp < m1[i]:
                    m1[i] = temp

            for ele in out2_2:
                temp = hashfun(ele, ran_st)
                if i not in m2 or temp < m2[i]:
                    m2[i] = temp

        for i in range(1, t):
            if m1[i] == m2[i]:
                simiValue += 1
        JS[k, r] = simiValue/t
        end = time.time()
        runTime[k, r] = end-start
print(JS)
print(runTime)
for i in range(5):
    plt.scatter(runTime[:, i], JS[:, i], label="t = "+str(T[i]), s=2)
plt.xlabel("run time (s)")
plt.ylabel("Approximate Jaccard similarity ")
plt.legend(loc="lower right")
plt.show()
