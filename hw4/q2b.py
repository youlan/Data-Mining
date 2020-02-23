
import numpy as np
import matplotlib.pyplot as plt

file = open("C2.txt","r")
lines = file.readlines()
data = []

for line in lines:
    data.append([float(line.split()[1]),float(line.split()[2])])
data = np.array(data)



centerCost = np.zeros(1000)
meanCost = np.zeros(1000)
allCenters = []
Gonzalez_phi = np.loadtxt("GoneIndex.txt")
Gindex1 = np.where(Gonzalez_phi == 0)
Gindex2 = np.where(Gonzalez_phi == 1)
Gindex3 = np.where(Gonzalez_phi == 2)
Gindex_sum = set([np.sum(Gindex1), np.sum(Gindex2), np.sum(Gindex3)])

count = 0
for iter in range(1000):
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
            dist = (centers[x][0]-data[j][0])**2+(centers[x][1]-data[j][1])**2
            prob_distribution.append(dist)

        prob_distribution = np.array(prob_distribution) / np.sum(prob_distribution)
        centers.append(data[np.random.choice(range(len(data)), p=prob_distribution)])
        i += 1

        for k in range(len(data)):
            x = int(phi[k])
            dist_x = np.sqrt((centers[x][0] - data[k][0]) ** 2 + (centers[x][1] - data[k][1]) ** 2)
            dist_i = np.sqrt((centers[i][0] - data[k][0]) ** 2 + (centers[i][1] - data[k][1]) ** 2)
            if (dist_x > dist_i):
                phi[k] = i
    #print(centers)
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

    centerCost[iter] = center_cost
    meanCost[iter] = mean_cost
    #print(phi)
    #if np.sum(phi) == np.sum(Gonzalez_phi):
    index1 = np.where(phi == 0)
    index2 = np.where(phi == 1)
    index3 = np.where(phi == 2)
    index_sum = set([np.sum(index1), np.sum(index2), np.sum(index3)])
    #print(index_sum)
    if index_sum == Gindex_sum:
        #print(index_sum,Gindex_sum)
        #print(phi)
        count += 1

print("The standard deviation of center cost: "+ str(np.std(centerCost)))
print("The standard deviation of mean cost: " + str(np.std(meanCost)))
print("The fraction of subsets similar to Gonzalez: "+str(count/len(meanCost)))
#print(len(meanCost))
fig, ax = plt.subplots(figsize=(8, 6))
n, bins, patches = ax.hist(meanCost, 100, density=True, histtype='step', cumulative=True)

ax.set_title('CDF of 3-mean cost')
ax.set_xlabel('3-mean cost')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

#colors = ["red", "green", "blue"]

