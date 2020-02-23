import math
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import time

def U2N():
    u1 = random.uniform(0,1)
    u2 = random.uniform(0,1)
    return np.sqrt(-2 * np.log(u1)) * math.cos(2 * math.pi * u2)

def normalize(v):
    norm = np.linalg.norm(v)
    return v/(norm**2)

def Angular(a,b):
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    x = np.dot(a,b)/(norma * normb)
    return 1 - math.acos(x)/math.pi


csvfile = open("R.csv", "r")
reader = csv.reader(csvfile)
data = np.zeros((500, 100))

for r, row in enumerate(reader):
    for c in range(len(row)):
        data[r, c] = float(row[c])
#print(data[0])
'''
vector = np.zeros((160,100))
for i in range(160):
    for j in range(100):
        y = U2N()
        vector[i,j] = y
    vector[i,:] = normalize(vector[i,:])
'''

dot_product = []
count = 0

start = time.time()
for i in range(500):
    for j in range(i+1, 500):
        #product = np.dot(vector[i,:],vector[j,:])
        #print(product)
        #AS = Angular(vector[i, :], vector[j, :])
        AS = Angular(data[i],data[j])
        dot_product.append(AS)
        if AS > 0.85:
            count += 1
print(count)
end = time.time()
print(end-start)

n_bins = 100
fig, ax = plt.subplots(figsize=(8, 6))
n, bins, patches = ax.hist(dot_product, n_bins, density=True, histtype='step', cumulative=True)

ax.set_title('CDF')
ax.set_xlabel('Angular Similarities')
ax.set_ylabel('Likelihood of occurrence')

plt.show()