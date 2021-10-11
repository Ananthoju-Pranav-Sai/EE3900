import numpy as np
import math
from matplotlib import pyplot as plt

def tr_1(t):
    if(t>=0 and t<=1):
        return t
    elif(t>=1 and t<=2):
        return 2-t
    else:
        return 0
def tr_2(t):
    if(t>=1 and t<=2):
        return t-1
    elif(t>=2 and t<=3):
        return 3-t
    else:
        return 0
def y(t):
    return tr_1(t)+tr_2(t)

t = np.linspace(-2, 5,400)
y_t = []
tr1 = []
tr2 = []
for i in t:
    tr1.append(tr_1(i))
    tr2.append(tr_2(i))
    y_t.append(y(i))

plt.plot(t,tr1,color='green',linestyle='--',label='$tr(t-1)$')
plt.plot(t,tr2,color='blue',linestyle='--',label='$tr(t-2)$')
plt.plot(t,y_t,color='red',label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid()
plt.show()