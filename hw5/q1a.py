import numpy as np

f1 = open("S1.txt", "r")
S1 = f1.readline()

f2 = open("S2.txt", "r")
S2 = f2.readline()

def MG(S,k=10):
    k=10
    count = np.zeros(k-1)
    label = ['' for i in range(k-1)]

    for char in S:
        if char in label:
            ind = label.index(char)
            count[ind] = count[ind]+1
        elif np.argwhere(count == 0.0).shape[0]:
            first_zero_ind = np.argwhere(count == 0)[0][0]
            label[first_zero_ind] = char
            count[first_zero_ind] = 1
        else:
            count = count-1
    return count, label

count, label = MG(S2, k=10)
print('  the length of set is %d'%(len(S2)))

print("label", "counters", "ratio")

for i in range(len(count)):
    print('%s & %d &  %f  '%(label[i],count[i],count[i]/len(S2)))
