from OrdenableIterativoAbstract import OrdenableIterativoAbstractClass;

class BurbujaMejorado(OrdenableIterativoAbstractClass):
    
    def ordenar(self,elementos):
        #self.imprimir(elementos)
        esta_ordenado = False;
        print(elementos)
        print("Empezando el algoritmo..")
        for i in range(0,len(elementos),1):
            print('\nIteracion: ' , i)
            if (not esta_ordenado):
                esta_ordenado = True
                for j in range(0,len(elementos)-i-1):
                    if(elementos[j] > elementos[j+1]):
                        esta_ordenado = False
                        self.intercambiar(elementos, j, j+1)
                    print(j,"->",elementos)
                    #self.imprimir(elementos)
            else:
                print("Sal......")
                break