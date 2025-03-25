import matplotlib.pyplot as plt
import numpy as np
e0 = 1

def momentB(p,l,a,c=1): #position, length of magnet, angle of magnet, charge
    pP = np.array(l/2*np.cos(a),l/2*np.sin(a))
    pM = np.array(-l/2*np.cos(a),-l/2*np.sin(a))
    p = np.array(p)
    dP = p-pP
    dM = p-pM
    mCP = np.cross(p,c**2/(4*np.pi*e0*dP**2)*(pP-p)) # Mo(P) = OM^L
    mCM = np.cross(p,c**2/(4*np.pi*e0*dM**2)*(pM-p))
    dLAdt = mCP+mCM
    return dLAdt


m = [[momentB((x,y),20,1) for x in range(0,255)] for y in range(0,255)]
plt.imshow(m)
plt.show()
