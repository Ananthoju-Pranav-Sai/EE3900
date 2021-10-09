import numpy as np
from matplotlib import pyplot as plt
import math

def g(t):
    if(t<2 and t>=0):
        return 1
    else :
        return 0

t = np.linspace(-2,3,500)
g_t = []
for i in t:
    g_t.append(g(i))

plt.plot(t,g_t)
plt.xlabel('t')
plt.ylabel('$g(t)$')
plt.grid()
plt.show()