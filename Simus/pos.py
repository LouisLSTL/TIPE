from SimMagnetometre import sim
import numpy as np
import matplotlib.pyplot as plt
grid = np.array([[(np.log(sim(0,np.array((x,y)), thetas = np.linspace(0,6*np.pi,1),l=3))[0]) for y in np.linspace(-5,5,100)] for x in np.linspace(-5,5,100)])

plt.imshow(grid)
plt.savefig('sim.png')