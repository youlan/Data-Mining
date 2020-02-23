import numpy as np
import matplotlib.pyplot as plt
import time

m = [400, 2000, 5000]
n = [100, 5075, 10050, 15025, 20000]
timelist1 = [0.7935013771057129, 80.92818903923035, 173.64442920684814, 269.8831284046173, 370.211811542511]
timelist2 = [3.993746757507324, 400.2399353981018, 867.7029836177826, 1339.0971188545227, 1858.364889383316]
timelist3 = [9.927703619003296, 1002.4264652729034, 2175.092712163925, 3355.2966163158417, 4355.2966163158417]


plt.plot(n, timelist1, marker="*", label="m = 400")
plt.plot(n, timelist2, marker="*", label="m = 2000")
plt.plot(n, timelist3, marker="*", label="m = 5000")
plt.title("Coupon Collection")
plt.xlabel("n")
plt.ylabel("time (s)")
plt.legend(loc="upper left")
plt.show()