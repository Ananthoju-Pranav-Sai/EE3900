import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
def X(k):
    if(k==0):
        return 2
    elif(k>=-3 and k<=3):
        return abs(k)
    else:
        return 0
k=np.linspace(-3, 3, num=7)
#plots
X_k=[]
for i in k:
  X_k.append(X(i))

plt.stem(k,X_k,use_line_collection=True)
plt.xlabel('$k$')
plt.ylabel('$X[k]$')
plt.text(3+0.1,14-.5,"$T$")
plt.grid()
plt.show()