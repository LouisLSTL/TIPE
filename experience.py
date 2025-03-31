import numpy as np



def omegaC(phi,eta,omega):
    a,b = np.polyfit(eta,np.sin(phi)/omega,1)
    return b        # KV/m0Be


def LorenzFarad(N,S,dBdt):
    return -N*S*dBdt

