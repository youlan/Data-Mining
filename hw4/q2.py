
import numpy as np
import matplotlib.pyplot as plt

file = open("C2.txt","r")
lines = file.readlines()
data = []

for line in lines:
    data.append([float(line.split()[1]),float(line.split()[2])])
data = np.array(data)

centers = [data[0]]

i = 0
phi = np.zeros(len(data))
index_set = set([1])

while i < 2:

    max_dist = 0
    for j in range(len(data)):
        x = int(phi[j])
        #print(centers[x][0])
        dist = np.sqrt((centers[x][0]-data[j][0])**2+(centers[x][1]-data[j][1])**2)
        if dist > max_dist:
            max_dist = dist
            center = data[j]
            index = j+1
    i += 1
    print(index)
    index_set.add(index)
    centers.append(center)

    for k in range(len(data)):
        x = int(phi[k])
        dist_x = np.sqrt((centers[x][0] - data[k][0]) ** 2 + (centers[x][1] - data[k][1]) ** 2)
        dist_i = np.sqrt((centers[i][0] - data[k][0]) ** 2 + (centers[i][1] - data[k][1]) ** 2)
        if (dist_x > dist_i):
            phi[k] = i
print(index_set)
clusters = [[],[],[]]
center_cost = 0
mean_cost = 0

for i in range(len(data)):
    x = int(phi[i])
    clusters[x].append(data[i])
    dist = np.sqrt((centers[x][0] - data[i][0]) ** 2 + (centers[x][1] - data[i][1]) ** 2)
    mean_cost += dist**2/len(data)
    if dist > center_cost:
        center_cost = dist

mean_cost = np.sqrt(mean_cost)
np.savetxt("GoneIndex.txt", phi)
print("3-center cost: "+str(center_cost))
print("3-mean cost: "+str(mean_cost))
print(centers)


colors = ["red", "green", "blue"]

fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(clusters, colors):
    #print(data)
    for dot in data:
        x,y = dot
       # print(x,y)
        ax.scatter(x, y, alpha=0.8, c=color)

plt.title("Gonzalez Clustering")
plt.show()
    #nce =
