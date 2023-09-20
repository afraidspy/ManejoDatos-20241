# -*- coding: utf-8 -*-
"""
@author: guest
"""

from OrdenableIterativoAbstract import OrdenableIterativoAbstractClass;

class Burbuja(OrdenableIterativoAbstractClass):

    def ordenar(self,elementos):
        #self.imprimir(elementos)
        print(elementos)
        print("Empezando el algoritmo..")
        for i in range(0,len(elementos),1):
            print('\nIteracion: ' , i)
            for j in range(0,len(elementos)-1,1):#(O(n))
                if(elementos[j] > elementos[j+1]):#O(1)
                    # aux = elementos[j]
                    # elementos[j] = elementos[j + 1]
                    # elementos[j + 1] = aux
                    self.intercambiar(elementos, j,j+1)
                
                print(j,"->",elementos)