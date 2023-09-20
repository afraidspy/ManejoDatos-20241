
from OrdenableIterativoAbstract import OrdenableIterativoAbstractClass;

class Seleccion(OrdenableIterativoAbstractClass):
    
    def ordenar(self,elementos):
        print(elementos)
        print("Empezando el algoritmo..")
        for i in range(0,len(elementos)):
            print('\nIteracion: ' , i)
            minimo = i
            for j in range(i+1, len(elementos),1):
                if(elementos[j] < elementos[minimo]):
                    minimo = j
            
            self.intercambiar(elementos, i, minimo)
            print(j,"->",elementos)

        