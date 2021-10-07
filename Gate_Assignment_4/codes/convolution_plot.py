import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

def u(t):
    if(t<0):
        return 0
    else:
        return 1
def f(t):
    return u(t)-u(t-1)
def g(t):
    return u(t)-u(t-2)

delta=1.0/3.0
t = np.linspace(-3, 3,20)
f_t=[]
g_t=[]
for i in t:
    f_t.append(f(i))
    g_t.append(g(i))

y_t = signal.convolve(f_t, g_t)*delta
plt.plot(np.arange(len(y_t))*delta-7+0.67, y_t)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()