import os
import numpy as np


def JS(a, b):
    inter = set(a).intersection(set(b))
    union = list(set(a).union(set(b)))
    return len(inter)/len(union)

f1 = open("D1.txt", "r")
f2 = open("D2.txt", "r")
f3 = open("D3.txt", "r")
f4 = open("D4.txt", "r")
string1 = f1.readlines()
string2 = f2.readlines()
string3 = f3.readlines()
string4 = f4.readlines()
f1.close()
f2.close()
f3.close()
f4.close()


out1_1 = [(string1[0][i: i + 2]) for i in range(0, len(string1[0])-2)]
out1_1 = sorted(set(out1_1))
out2_1 = [(string2[0][i: i + 2]) for i in range(0, len(string2[0])-2)]
out2_1 = sorted(set(out2_1))
out3_1 = [(string3[0][i: i + 2]) for i in range(0, len(string3[0])-2)]
out3_1 = sorted(set(out3_1))
out4_1 = [(string4[0][i: i + 2]) for i in range(0, len(string4[0])-2)]
out4_1 = sorted(set(out4_1))
out1_2 = [(string1[0][j:j + 3]) for j in range(0, len(string1[0])-2)]
out1_2 = sorted(set(out1_2))
out2_2 = [(string2[0][j:j + 3]) for j in range(0, len(string2[0])-2)]
out2_2 = sorted(set(out2_2))
out3_2 = [(string3[0][j:j + 3]) for j in range(0, len(string3[0])-2)]

out3_2 = sorted(set(out3_2))
out4_2 = [(string4[0][j:j + 3]) for j in range(0, len(string4[0])-2)]
out4_2 = sorted(set(out4_2))



word1 = string1[0].split()
out1_3 = [(word1[i]+" "+word1[i+1]) for i in range(0, len(word1)-1, 1)]
out1_3 = sorted(set(out1_3))
word2 = string2[0].split()
out2_3 = [(word2[i]+" "+word2[i+1]) for i in range(0, len(word2)-1, 1)]
out2_3 = sorted(set(out2_3))
word3 = string3[0].split()
out3_3 = [(word3[i]+" "+word3[i+1]) for i in range(0, len(word3)-1, 1)]
out3_3 = sorted(set(out3_3))
word4 = string4[0].split()
out4_3 = [(word4[i]+" "+word4[i+1]) for i in range(0, len(word4)-1, 1)]
out4_3 = sorted(set(out4_3))
print(out4_3)

print(len(out1_1), len(out1_2), len(out1_3))
print(len(out2_1), len(out2_2), len(out2_3))
print(len(out3_1), len(out3_2), len(out3_3))
print(len(out4_1), len(out4_2), len(out4_3))


JSvalues = np.zeros((3, 6))


JSvalues[0, 0] = JS(out1_1, out2_1)
JSvalues[0, 1] = JS(out1_1, out3_1)
JSvalues[0, 2] = JS(out1_1, out4_1)
JSvalues[0, 3] = JS(out2_1, out3_1)
JSvalues[0, 4] = JS(out2_1, out4_1)
JSvalues[0, 5] = JS(out3_1, out4_1)


JSvalues[1, 0] = JS(out1_2, out2_2)
JSvalues[1, 1] = JS(out1_2, out3_2)
JSvalues[1, 2] = JS(out1_2, out4_2)
JSvalues[1, 3] = JS(out2_2, out3_2)
JSvalues[1, 4] = JS(out2_2, out4_2)
JSvalues[1, 5] = JS(out3_2, out4_2)

JSvalues[2, 0] = JS(out1_3, out2_3)
JSvalues[2, 1] = JS(out1_3, out3_3)
JSvalues[2, 2] = JS(out1_3, out4_3)
JSvalues[2, 3] = JS(out2_3, out3_3)
JSvalues[2, 4] = JS(out2_3, out4_3)
JSvalues[2, 5] = JS(out3_3, out4_3)

print(JSvalues)