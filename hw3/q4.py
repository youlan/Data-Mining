import hashlib, sys
import random, string
import time
import numpy as np
import matplotlib.pyplot as plt



start = time.time()
m1 = {}
m2 = {}
salt = []
simiValue = 0
for i in range(1, 160):
    ran_st = ''.join(random.sample(string.ascii_letters + string.digits, 5))
           #print(ran_st)
            for ele in out1_2:
                temp = hashfun(ele, ran_st)
                if i not in m1 or temp < m1[i]:
                    m1[i] = temp

            for ele in out2_2:
                temp = hashfun(ele, ran_st)
                if i not in m2 or temp < m2[i]:
                    m2[i] = temp

        for i in range(1, t):
            if m1[i] == m2[i]:
                simiValue += 1
        JS[k, r] = simiValue/t
        end = time.time()
        runTime[k, r] = end-start