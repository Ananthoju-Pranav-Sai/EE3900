import numpy as np
import math

V = np.array([[1,0],[0,0]])
u = np.array([-2,-1/2])
f = 4
n = np.array([-4,2])
p1 = np.array([0,2])
k = (p1.T@u)/(p1.T@n)

t = np.array([k*n.T+u.T])

A = np.concatenate((t,V))
B = np.append(np.array([-f]),k*n-u)

q = np.linalg.lstsq(A,B,rcond=0)[0]     #as here A is not a square matrix we aren't using np.linalg.solve
print(q)