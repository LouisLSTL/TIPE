import numpy as np
import matplotlib.pyplot as plt
# coords : (x,y) 
p = 1
r = np.array((3,0))
pn,ps = np.array((.5,0)),np.array((-.5,0))
alpha = 15
retard = alpha*np.pi/180
def rotMatr(theta,v):
    return np.matmul(np.array([
        (np.cos(theta),-np.sin(theta)),
        (np.sin(theta),np.cos(theta))]
    ),v)
def H(r,ps,pn):
    l = pn-ps
    m = np.dot(p,l)
    A =  3*r*(np.dot(m,r))
    B = np.linalg.norm(r)**5
    C = m/(np.linalg.norm(r)**3)
    return ((A)/(B) - (C))/(4*np.pi)


thetas = np.linspace(0,6*np.pi,1000)
pN = [rotMatr(thetas[i],pn) for i in range(len(thetas))]
pS = [rotMatr(thetas[i],ps) for i in range(len(thetas))]
h = [H(r,pS[i],pN[i]) for i in range(len(pS))] 

pN2 = [rotMatr(thetas[i]-retard,pn) for i in range(len(thetas))]
pS2 = [rotMatr(thetas[i]-retard,ps) for i in range(len(thetas))]
h2 = [H(r,pS2[i],pN2[i]) for i in range(len(pS2))] 

N = np.array([np.linalg.norm(i) for i in h])
a =  np.array([np.arctan2(*i) for i in h])
N2 =  np.array([np.linalg.norm(i) for i in h2])
a2 =  np.array([np.arctan2(*i) for i in h2])

fig=plt.figure()


ax1=fig.add_subplot(2,1,1)
ax1.plot(thetas,N+N2, 'r')
ax1.set_title('Norm of measured magnetic field')
ax1.set_xlabel(r'$\theta (rad)$')
ax2=fig.add_subplot(2,1,2)
ax2.plot(thetas,a+a2 ,'b')
ax2.set_title('Angle measured magnetic field direction')
ax2.set_xlabel(r'$\theta (rad)$')

fig.suptitle(r'pour $\theta$'+f' = {alpha} deg') 
plt.tight_layout()
plt.show()
plt.savefig('sim.png')