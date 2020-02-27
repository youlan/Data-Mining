import numpy as np

f1 = open("S1.txt", "r")
S1 = f1.readline()

f2 = open("S2.txt", "r")
S2 = f2.readline()

def query_count_min(counts, char):
    result_list = []
    t = counts.shape[0]
    k = counts.shape[1]
    for j in range(t):
        hash_ind = hash(char+str(j)) % k
        result_list.append(counts[j][hash_ind])
    return min(result_list)

k=10
t=5
counts = np.zeros((t,k))

for char in S2:
    for j in range(t):
        hash_ind = hash(char+str(j)) % k
        counts[j][hash_ind] = counts[j][hash_ind]+1

query_list = ['a','b','c']
print('  len of S2 set is ',len(S2))

for item in query_list:
    es_count = query_count_min(counts,item)
    print("%s & %d & %f" %(item, es_count, es_count/len(S2)))

