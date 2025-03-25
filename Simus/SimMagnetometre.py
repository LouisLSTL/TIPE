import numpy as np
mu0 = 4*np.pi*1e-7
# coords : (x,y) 

def Hall(B,I=np.array((-1,0,0)),Rh=3,t=1):
    Bext = np.concatenate((B,np.array([[0] for i in range(len(B))])),axis=1) #3e dim
    print(Bext)
    return np.array([np.linalg.norm(Rh*np.matmul(I/t,Be)) for Be in Bext])

def base(r=np.array((3,0)),p=1,thetas = np.linspace(0,6*np.pi,1000)):
    pn,ps = np.array((.5,0)),np.array((-.5,0))
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

    pN = [rotMatr(thetas[i],pn) for i in range(len(thetas))]
    pS = [rotMatr(thetas[i],ps) for i in range(len(thetas))]
    h = [H(r,pS[i],pN[i]) for i in range(len(pS))] 

    N = np.array([np.linalg.norm(i) for i in h])
    a =  np.array([np.arctan2(*i) for i in h])
    return N,a

def sim(a,r=np.array((3,0)),p=1,thetas = np.linspace(0,6*np.pi,1000),l=1,returnB=False):
    pn,ps = np.array((l/2,0)),np.array((-l/2,0))
    alpha = a
    retard = alpha*np.pi/180 
    def rotMatr(theta,v):#matrice de rotation
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

    pN = [rotMatr(thetas[i],pn) for i in range(len(thetas))] #poles tournés
    pS = [rotMatr(thetas[i],ps) for i in range(len(thetas))]
    h = [H(r,pS[i],pN[i]) for i in range(len(pS))] #champ vect en fonction de la rotation

    pN2 = np.array([rotMatr(thetas[i]-retard,pn) for i in range(len(thetas))]) #idem pour 2e aimant
    pS2 = np.array([rotMatr(thetas[i]-retard,ps) for i in range(len(thetas))])
    h2 = np.array([H(r,pS2[i],pN2[i]) for i in range(len(pS2))])

    htot = h+h2 #hypothese
    Ntot = np.array([np.linalg.norm(i) for i in htot]) #calculs norme et dir
    atot = np.array([(np.arctan2(*i)) if i[0]!=0 else np.arcsin(i[1]/np.linalg.norm(i)) for i in htot])
    return (Ntot,atot) if not returnB else htot*mu0
    """fig=plt.figure()


    ax1=fig.add_subplot(2,1,1)
    ax1.plot(thetas,Ntot, 'r')
    ax1.set_title('Norm of measured magnetic field')
    ax1.set_xlabel(r'$\theta (rad)$')
    ax2=fig.add_subplot(2,1,2)
    ax2.plot(thetas,atot ,'b')
    ax2.set_title('Angle measured magnetic field direction')
    ax2.set_xlabel(r'$\theta (rad)$')

    fig.suptitle(r'pour $\theta$'+f' = {alpha} deg') 
    plt.tight_layout()
    plt.show()
    plt.savefig('sim.png')"""