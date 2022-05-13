import matplotlib.pyplot as plt
import numpy as np
def f(x,a):
    return a/x
xlist=np.linspace(-10,10,num=1000)
ylist=f(xlist,3)
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
plt.show()

