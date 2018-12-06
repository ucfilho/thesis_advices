import numpy as np
import FOBJ

def PART(X,PBEST):
    rows = len(X)
    YCAL=FOBJ.OBJ(PBEST)
    NEW=FOBJ.OBJ(X)
    for i in range(rows):
        if(YCAL[i]>NEW[i]):
            PBEST[i,]=X[i,]
    return PBEST