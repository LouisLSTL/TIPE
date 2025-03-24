import matplotlib.pyplot as plt



def momentB(p,l,a): #position, length of magnet, angle of magnet
    pP = np.array(l/2*np.cos(a),l/2*np.sin(a))
    pM = np.array(-l/2*np.cos(a),-l/2*np.sin(a))
    p = np.array(p)
    dP = p-pP
    dM = p-pM
    mP = moeent en moins puis plus puis les 2 et on applique au mdele du barreau aimenté