from Simus.SimMagnetometre import sim,base
import numpy as np
import matplotlib.pyplot as plt
thetas = np.linspace(0,6*np.pi,1000)
for n in range(0,180,25):
    plt.plot(thetas,sim(n)[0],label=r'$\theta$'+f' = {n} deg')
plt.plot(thetas,base()[0],'k--',label='just stirrer')
plt.legend()
plt.grid()
plt.savefig('../demo.png')