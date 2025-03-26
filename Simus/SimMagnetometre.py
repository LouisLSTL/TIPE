import numpy as np
mu0 = 4*np.pi*1e-7
# coords : (x,y) 

def rotMatr(theta,v):
        return np.matmul(v, np.array(
             [
             [np.cos(theta),-np.sin(theta)],
             [np.sin(theta),np.cos(theta)]
             ]).T)


print(rotMatr(np.linspace(0,6*np.pi,1000),np.array((0,1))))

def Hall(B,I=np.array((-1,0,0)),Rh=3,t=1):
    Bext = np.concatenate((B,np.array([[0] for i in range(len(B))])),axis=1) #3e dim
    print(Bext)
    return np.array([np.linalg.norm(Rh*np.matmul(I/t,Be)) for Be in Bext])

def base(r=np.array((3,0)),p=1,thetas = np.linspace(0,6*np.pi,1000)):
    pn,ps = np.array((.5,0)),np.array((-.5,0))
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
    def H(r,ps,pn):
        l = pn-ps
        m = p*l
        A =  3*r*(np.dot(m,r))
        B = np.linalg.norm(r)**5
        C = m/(np.linalg.norm(r)**3)
        return ((A)/(B) - (C))/(4*np.pi)

    pN = rotMatr(thetas,pn) #poles tournés
    pS = rotMatr(thetas,ps)
    h = H(r,pS,pN) #champ vect en fonction de la rotation

    pN2 = rotMatr(thetas-retard,pn)  #idem pour 2e aimant
    pS2 = rotMatr(thetas-retard,ps)
    h2 = H(r,pS2,pN2)

    htot = h+h2 #hypothese
    Ntot = np.apply_along_axis(np.linalg.norm,0,htot)
    
    #Ntot = np.array([np.linalg.norm(i) for i in htot]) #calculs norme et dir
    atot = np.array([(np.arctan2(*i)) if i[0]!=0 else np.arcsin(i[1]/np.linalg.norm(i)) for i in htot]) #dernier à enlever
    return (Ntot,atot) if not returnB else htot*mu0