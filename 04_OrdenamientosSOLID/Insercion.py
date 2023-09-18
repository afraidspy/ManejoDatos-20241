# -*- coding: utf-8 -*-
"""

@author: Jessica
"""

from OrdenableIterativoAbstract import OrdenableIterativoAbstractClass;

class Insercion(OrdenableIterativoAbstractClass):
    
    def ordenar(self,elementos):
       print(elementos)
       print("Empezando el algoritmo de Inserción..")
 
       for i in range(1,len(elementos)):
           aux = elementos[i]
           print('\nIteracion: ' , i)
           for j in range(i-1, -1,-1):
               #print("\ni={}j={} ".format( i,j))
               if (elementos[j]>aux):
                   # elementos[j+1] = elementos[j]
                   # elementos[j] = aux
                   # print(elementos)
                      self.intercambiar(elementos, j, j+1)
               print(j,"->",elementos)
