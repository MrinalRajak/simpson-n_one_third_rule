

#simpson's one third rule(fixed step size) usig scipy module of python.

import numpy as np
from scipy.integrate import simps
xs,h=np.linspace(0,1.57,11,retstep=True)
ys=np.array([0.0000,0.1564,0.3090,0.4540,0.5878,0.7071,0.8090,0.8910,0.9511,0.9877,1.0000],dtype=float)

i=(h/3)*(ys[0]+ys[-1]+4*np.sum(ys[1:-1:2])+2*np.sum(ys[2:-1:2]))
print ("Algorithm based composite simpson's (1/3)rd rule Result: ",i)
print ("Scipy based integrated result: ",simps(ys,dx=h))
