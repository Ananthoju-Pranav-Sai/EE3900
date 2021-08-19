from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

A = np.array([3,5,4]).reshape((3,1))
B = np.array([-1,1,2]).reshape((3,1))
C = np.array([-5,-5,-2]).reshape((3,1))

AB = B-A
BC = C-B
CA = A-C

print('Vector AB is :\n',AB)
print('Vector BC is :\n',BC)
print('Vector CA is :\n',CA)

L_AB = np.empty((2,3),float)
L_AB[0,:] = A[:,0]
L_AB[1,:] = B[:,0]

L_BC = np.empty((2,3),float)
L_BC[0,:] = B[:,0]
L_BC[1,:] = C[:,0]

L_CA = np.empty((2,3),float)
L_CA[0,:] = C[:,0]
L_CA[1,:] = A[:,0]

plt.plot(L_AB[:,0],L_AB[:,1],L_AB[:,2],'r',label="AB")
plt.plot(L_BC[:,0],L_BC[:,1],L_BC[:,2],'g',label="BC")
plt.plot(L_CA[:,0],L_CA[:,1],L_CA[:,2],'b',label="CA")

ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.text(3,5,4, "A", color='red')
ax.text(-1,1,2, "B", color='red')
ax.text(-5,-5,-2, "C", color='red')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()