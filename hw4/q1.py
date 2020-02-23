import numpy as np
import matplotlib.pyplot as plt

def single_link(cluster1, cluster2):
    min_dist = np.inf
    for i in cluster1:
        for j in cluster2:
            dist = np.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)
            if dist < min_dist:
                min_dist = dist
    return min_dist

def compelete_link(cluster1, cluster2):
    max_dist = -np.inf
    for i in cluster1:
        for j in cluster2:
            dist = np.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)
            if dist > max_dist:
                max_dist = dist
    return max_dist

def mean_link(cluster1, cluster2):
    dot1 = np.sum(cluster1, axis=0)/len(cluster1)
    dot2 = np.sum(cluster2, axis=0)/len(cluster2)
    return np.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)


def distMeature(node,rule):
    n = len(node)
    distance = np.ones((n,n))*np.inf
    for i in range(len(node)):
        for j in range(i+1, len(node)):
            if rule =="single":
                distance[i,j] = single_link(node[i], node[j])
            elif rule == "complete":
                distance[i, j] = compelete_link(node[i], node[j])
            elif rule == "mean":
                distance[i,j] = mean_link(node[i],node[j])
    return distance

file = open("C1.txt","r")
lines = file.readlines()
data1 =[]
data2 =[]
data3 =[]
for line in lines:
    data1.append([[float(line.split()[1]),float(line.split()[2])]])
    data2.append([[float(line.split()[1]), float(line.split()[2])]])
    data3.append([[float(line.split()[1]), float(line.split()[2])]])

#print(data)
cluster_single = data1

print(cluster_single)
while len(cluster_single) > 4:
    distance = distMeature(cluster_single, "single")
    index = np.where(distance == np.min(distance))
    cluster_single[index[0][0]].extend(cluster_single[index[1][0]])
    del cluster_single[index[1][0]]


cluster_complete = data2
print(cluster_complete)
while len(cluster_complete) > 4:
    distance = distMeature(cluster_complete, "complete")
    index = np.where(distance == np.min(distance))
    #print(index[0][0], index[1][0])
    cluster_complete[index[0][0]].extend(cluster_complete[index[1][0]])
    del cluster_complete[index[1][0]]

cluster_mean = data3
print(cluster_mean)
while len(cluster_mean) > 4:
    distance = distMeature(cluster_mean, "mean")
    index = np.where(distance == np.min(distance))
    #print(index[0][0])

    cluster_mean[index[0][0]].extend(cluster_mean[index[1][0]])
    #print(cluster_mean[index[0][0]])
    del cluster_mean[index[1][0]]
    #print(cluster_mean)

colors = ["red", "green", "blue", "orange"]

fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(cluster_single, colors):
    for dot in data:
        x,y = dot
        ax.scatter(x, y, alpha=0.8, c=color)

plt.title("Single-Link")
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(cluster_complete, colors):
    #print(data)
    for dot in data:
        x,y = dot
        #print(x,y)
        ax.scatter(x, y, alpha=0.8, c=color)

plt.title("Complete-Link")
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(cluster_mean, colors):
    #print(data)
    for dot in data:
        x,y = dot
       # print(x,y)
        ax.scatter(x, y, alpha=0.8, c=color)

plt.title("Mean-Link")
plt.show()
#print(cluster_mean)


