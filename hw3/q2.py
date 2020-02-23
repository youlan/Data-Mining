import math
import random
import numpy as np
import matplotlib.pyplot as plt


def U2N():
    u1 = random.uniform(0,1)
    u2 = random.uniform(0,1)
    return np.sqrt(-2 * np.log(u1)) * math.cos(2 * math.pi * u2)

def normalize(v):
    norm = np.linalg.norm(v)
    return v/(norm)

vector = np.zeros((160,100))

for i in range(160):
    for j in range(100):
        y = U2N()
        vector[i,j] = y
    vector[i,:] = normalize(vector[i,:])

dot_product = []
for i in range(160):
    for j in range(i+1, 160):
        product = np.dot(vector[i,:],vector[j,:])
        #print(product)
        dot_product.append(product)

n_bins = 100
fig, ax = plt.subplots(figsize=(8, 6))
n, bins, patches = ax.hist(dot_product, n_bins, density=True, histtype='step', cumulative=True)

ax.set_title('CDF')
ax.set_xlabel('Dot products for each pairs of t = 160')
ax.set_ylabel('Likelihood of occurrence')

plt.show()