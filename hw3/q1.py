
import math
import matplotlib.pyplot as plt

def LSH(s,b,r):
    return 1-pow((1-pow(s, b)),r)

slist = [0.77, 0.25, 0.2, 0.33, 0.55, 0.91]

X = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.85, 0.9,0.95, 1.0]
Y = []
for i in range(len(slist)):
    s_value = slist[i]
    lsh_value = LSH(s_value,32,5)
    print(lsh_value)

for j in range(len(X)):
    s_value = X[j]
    lsh_value = LSH(s_value, 32,5)
    Y.append(lsh_value)

plt.plot(X,Y)
plt.xlabel("JS value")
plt.ylabel("LSH value")
plt.show()