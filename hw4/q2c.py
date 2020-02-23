
import numpy as np
import matplotlib.pyplot as plt

file = open("C2.txt","r")
lines = file.readlines()
data = []

for line in lines:
    data.append([float(line.split()[1]),float(line.split()[2])])
data = np.array(data)

centers = [data[0], data[1], data[2]]
#centers = [data[0], data[1039], data[646]]
centerCost = []
meanCost = []
iter = 0
while iter < 100:

    cluster1 = []
    cluster2 = []
    cluster3 = []
    phi = np.zeros(len(data))
    for i in range(len(data)):
        dist1 = np.sqrt((centers[0][0] - data[i][0]) ** 2 + (centers[0][1] - data[i][1]) ** 2)
        dist2 = np.sqrt((centers[1][0] - data[i][0]) ** 2 + (centers[1][1] - data[i][1]) ** 2)
        dist3 = np.sqrt((centers[2][0] - data[i][0]) ** 2 + (centers[2][1] - data[i][1]) ** 2)
        min_dist = min(dist1,dist2,dist3)
        if min_dist == dist1:
            phi[i] = 0
            cluster1.append(data[i])
        elif min_dist == dist2:
            phi[i] = 1
            cluster2.append(data[i])
        elif min_dist == dist3:
            phi[i] = 2
            cluster3.append(data[i])

    centers[0] = np.mean(cluster1, axis=0)
    centers[1] = np.mean(cluster2, axis=0)
    centers[2] = np.mean(cluster3, axis=0)
    print(centers)
    iter += 1



clusters = [cluster1,cluster2,cluster3]

meanCost = 0
for i in range(len(clusters)):

    center = centers[i]
    for j in range(len(clusters[i])):
        dot = clusters[i][j]
        meanCost += ((dot[0]-center[0])**2 + (dot[1]-center[1])**2)/len(data)

meanCost = np.sqrt(meanCost)
print()
print("The 3-mean cost of Lloyd's k-means clustering: " + str(meanCost))

colors = ["red", "green", "blue"]

fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(clusters, colors):
    #print(data)
    for dot in data:
        x,y = dot
       # print(x,y)
        ax.scatter(x, y, alpha=0.8, c=color)

plt.title("Lloyd's k-means clustering")
#plt.title("Lloyd's k-means clustering with Gonzalez initialized")
plt.show()
