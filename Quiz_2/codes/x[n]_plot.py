import numpy as np
from matplotlib import pyplot as plt

a=2
N=10

def u(n):
    if(n>=0):
        return 1
    return 0

def x(n):
    if(n>=0 and n<=N-1):
        return 1
    return 0

def h(n):
    if(n>=0):
        return a**n
    return 0

def g(n):
    return (1-a**(n+1))*u(n)/(1-a)

def y(n):
    return g(n)-g(n-N)

n=np.linspace(0,15,15)
x_n=[]
y_n=[]
h_n=[]

for i in n:
    x_n.append(x(i))
    h_n.append(h(i))
    y_n.append(y(i))

plt.stem(n,x_n,use_line_collection=True)
plt.ylabel('$x[n]$')
plt.xlabel('$n$')
plt.show()

