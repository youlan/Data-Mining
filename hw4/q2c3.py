
import numpy as np
import matplotlib.pyplot as plt

file = open("C2.txt","r")
lines = file.readlines()
data = []

for line in lines:
    data.append([float(line.split()[1]),float(line.split()[2])])
data = np.array(data)

#centerCost = np.zeros(100)
#meanCost = np.zeros(100)
allCenters = []
#Gonzalez_index = set([1040, 1, 647])
count = 0
meanCosts = np.zeros(100)

for t in range(100):
    #x = np.random.randint(len(data))

    centers = [data[0]]
    i = 0
    phi = np.zeros(len(data))
    #index_set = set([1])


    while i < 2:
        #max_dist = 0
        prob_distribution = []
        for j in range(len(data)):
            x = int(phi[j])
            #print(centers[x][0])
            dist = np.sqrt((centers[x][0]-data[j][0])**2+(centers[x][1]-data[j][1])**2)
            prob_distribution.append(dist)

        i += 1
        prob_distribution = np.array(prob_distribution) / np.sum(prob_distribution)
        centers.append(data[np.random.choice(range(len(data)), p=prob_distribution)])

        for k in range(len(data)):
            x = int(phi[k])
            dist_x = np.sqrt((centers[x][0] - data[k][0]) ** 2 + (centers[x][1] - data[k][1]) ** 2)
            dist_i = np.sqrt((centers[i][0] - data[k][0]) ** 2 + (centers[i][1] - data[k][1]) ** 2)
            if (dist_x > dist_i):
                phi[k] = i
    Kindex1 = np.where(phi == 0)
    Kindex2 = np.where(phi == 1)
    Kindex3 = np.where(phi == 2)
    Kindex_sum = set([np.sum(Kindex1), np.sum(Kindex2), np.sum(Kindex3)])

    iter = 0
    while iter < 50:
        cluster1 = []
        cluster2 = []
        cluster3 = []
        phi = np.zeros(len(data))
        for i in range(len(data)):
            dist1 = np.sqrt((centers[0][0] - data[i][0]) ** 2 + (centers[0][1] - data[i][1]) ** 2)
            dist2 = np.sqrt((centers[1][0] - data[i][0]) ** 2 + (centers[1][1] - data[i][1]) ** 2)
            dist3 = np.sqrt((centers[2][0] - data[i][0]) ** 2 + (centers[2][1] - data[i][1]) ** 2)
            min_dist = min(dist1, dist2, dist3)
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
        # print(centers)
        iter += 1

    Lindex1 = np.where(phi == 0)
    Lindex2 = np.where(phi == 1)
    Lindex3 = np.where(phi == 2)
    Lindex_sum = set([np.sum(Lindex1), np.sum(Lindex2), np.sum(Lindex3)])

    if Kindex_sum == Lindex_sum:
        count+=1

    clusters = [cluster1, cluster2, cluster3]

    meanCost = 0
    for i in range(len(clusters)):

        center = centers[i]
        for j in range(len(clusters[i])):
            dot = clusters[i][j]
            meanCost += ((dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2) / len(data)

    meanCost = np.sqrt(meanCost)
    meanCosts[t] = meanCost
#print(count/100)
print("The fraction of subsets similar to Gonzalez: "+str(count/100))
print(meanCosts)

fig, ax = plt.subplots(figsize=(8, 6))
n, bins, patches = ax.hist(meanCosts, 100, density=True, histtype='step', cumulative=True)

ax.set_title('CDF of Lloyds with k-Mean++ output')
ax.set_xlabel('cost')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

colors = ["red", "green", "blue"]
fig = plt.figure()
ax = fig.add_subplot()
for data, color in zip(clusters, colors):
    #print(data)
    for dot in data:
        x,y = dot
       # print(x,y)
        ax.scatter(x, y, alpha=0.8, c=color)

#plt.title("Lloyd's k-means clustering")
plt.title("Lloyd's k-means clustering with Gonzalez initialized")
plt.show()