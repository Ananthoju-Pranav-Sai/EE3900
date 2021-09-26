import numpy as np
import matplotlib.pyplot as plt

def parabola(x):
    return (x-2)**2

def line_(x):
    return 2*x-5

x=np.linspace(-10,10,60)

plt.plot(x[30:],line_(x[30:]),'g',label="$2x-y=5$")
plt.plot(x,parabola(x),'r',label="$y=(x-2)^2$")
plt.scatter(3,1,label="point of tangency")
plt.text(3+0.1,1-.1,"$(3,1)$")
plt.grid()
plt.legend()
plt.show()