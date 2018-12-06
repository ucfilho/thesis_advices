
"""
Created on Fri Dec 06 2017
@author: ucfilho
"""
import numpy as np
import PSOnew


W=0.75
C1=2
C2=2
NPAR=100 #PARTICULAS
ITE=100 #ITERACOES
PAR=2 #NUM DE PARAMETROS A SER OTIMIZADOS
MAX=[5,5] # MAXIMO DE CADA PARAMETRO
MIN=[-4,-4] # MINIMO DE CADA PARAMETRO

#resp=PSOnew.PSO(W,C1,C2,NPAR,ITE,PAR,MAX,MIN)
resp,best=PSOnew.PSO(W,C1,C2,NPAR,ITE,PAR,MAX,MIN)

for i in range(ITE):
    if((i+1)%10==0):
        print("iteracao=",i+1,"f obj=",resp[i])
print(best)