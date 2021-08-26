from math import cos
import numpy as np
import math
from matplotlib import pyplot as plt

P = np.array([0,0])
L = np.array([4,0])

a = 4
b = 6.5
theta = np.pi/2
beta = 110*np.pi/180
gamma = 85*np.pi/180
alpha = 2*np.pi-(theta+beta+gamma)

e = np.sqrt(a*a+b*b-2*a*b*math.cos(alpha))
d = e*math.sin(beta-np.arcsin(a*math.sin(alpha)/e))/math.sin(gamma)

A = L + b*np.array([math.cos(np.pi-alpha),math.sin(np.pi-alpha)])
N = d*np.array([math.cos(theta),math.sin(theta)])

plt.plot(P[0],P[1],'o')
plt.text(P[0]+0.1,P[1]+0.1,'P')

plt.plot(L[0],L[1],'o')
plt.text(L[0]+0.1,P[1]-0.1,'L')

plt.plot(A[0],A[1],'o')
plt.text(A[0]+0.1,A[1]-0.1,'A')

plt.plot(N[0],N[1],'o')
plt.text(N[0]+0.1,N[1]-0.1,'N')

plt.plot([P[0],L[0]],[P[1],L[1]],label="PL")
plt.plot([L[0],A[0]],[L[1],A[1]],label="LA")
plt.plot([A[0],N[0]],[A[1],N[1]],label="AN")
plt.plot([N[0],P[0]],[N[1],P[1]],label="NP")
plt.plot([P[0],A[0]],[P[1],A[1]],label="PA")

plt.grid()
plt,plt.legend()
plt.show()