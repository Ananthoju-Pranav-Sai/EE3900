import numpy as np
import math
from matplotlib import pyplot as plt

def y(t):
    return 5*(1-math.exp(-2*t))

t = np.linspace(0,10,50)
y_t=[]
for i in t:
    y_t.append(y(i))
plt.plot(t,y_t)
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
