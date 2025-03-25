from SimMagnetometre import sim,base,Hall
import numpy as np
import matplotlib.pyplot as plt

thetas = np.linspace(0,6*np.pi,1000)
for n in range(0,180,20):
    plt.plot(thetas,(Hall(sim(n,returnB=True))),label=r'$\theta$'+f' = {n} deg')
#plt.plot(thetas,Hall(base()),'k--',label='just stirrer')
plt.legend()
plt.grid()
plt.savefig('demo.png')