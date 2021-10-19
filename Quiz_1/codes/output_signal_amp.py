import numpy as np 
import math
from matplotlib import pyplot as plt


n = np.linspace(0,10,11,endpoint=True)

y=[]
x=[]
for i in n:
    y.append(8*np.e**(1j*np.pi/4)*math.cos(math.pi*(i-1)/2))
    x.append(math.cos(math.pi*i/2))

plt.stem(n,np.abs(y))
plt.grid()
plt.xlabel("n")
plt.ylabel("|y(n)|")

plt.show()