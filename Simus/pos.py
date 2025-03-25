from SimMagnetometre import sim, Hall
import numpy as np
import matplotlib.pyplot as plt


grid = np.zeros((100,100))
ax = np.linspace(-100,100,100)
min = 10000
for x in range(100):
    for y in range(100):
        v = Hall(sim(0,np.array((ax[x],ax[y])), thetas = np.linspace(0,6*np.pi,1),l=.1,returnB=True))
        min = v if v<min else min
        grid[x][y]=v
grid+=abs(min)+1


plt.imshow(np.log(grid))
plt.colorbar()
plt.savefig('sim.png')