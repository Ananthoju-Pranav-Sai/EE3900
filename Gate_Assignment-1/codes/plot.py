import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
def a(k):
    if(k==0):
        return 2
    elif(k>=-3 and k<=3):
        return abs(k)
    else:
        return 0
k=np.linspace(-3, 3, num=7)
#plots
a_k=[]
for i in k:
  a_k.append(a(i))

plt.stem(k,a_k,use_line_collection=True)
plt.xlabel('$k$')
plt.ylabel('$a_k$')
plt.grid()
plt.show()