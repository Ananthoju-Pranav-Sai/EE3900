import numpy as np 
import math
from matplotlib import pyplot as plt
def x(t):
    w = 2*np.pi/6 
    return 2+6*math.cos(3*w*t)+4*math.cos(2*w*t)+2*math.cos(w*t)


t = np.linspace(-12,12,500)
x_t = []
for i in t:
    x_t.append(x(i))

y = np.linspace(-8, 13,3)
plt.plot(t,x_t)
plt.grid()
plt.annotate(text='', xy=(0,14), xytext=(6,14), arrowprops=dict(arrowstyle='<->'))
plt.xticks([-12,-6,0,6,12])
plt.text(2.2,14+.2,"$T=6$")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()
1