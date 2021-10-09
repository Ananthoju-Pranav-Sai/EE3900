import numpy as np
from matplotlib import pyplot as plt
import math

def f(t):
    if(t<1 and t>=0):
        return 1
    else :
        return 0

t = np.linspace(-1,2,500)
f_t = []
for i in t:
    f_t.append(f(i))

plt.plot(t,f_t)
plt.xlabel('t')
plt.ylabel('$f(t)$')
plt.grid()
plt.show()