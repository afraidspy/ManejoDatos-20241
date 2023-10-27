from ABBAbstract import  ArbolBuscable
from Nodo import Nodo
    
"""
Se implementa la clase ABB
"""
class ABB(ArbolBuscable):
    def __init__(self):
        self.raiz = None
        self.cuantos = 0
    
    def esta_vacio(self):
        return self.cuantos == 0;
    
    def vaciar(self):
        self.raiz = None
        self.cuantos = 0
   
    def tamanio(self):
        return self.cuantos
    
    def agregar(self,elemento):
        self.aux_agregar(elemento,self.raiz)
        print("Raíz:: ", self.raiz)
        
    def aux_agregar(self,elemento,nodo):
        if nodo==None:
            nodo = Nodo(elemento)
            print("Add: ",nodo)
            if self.cuantos == 0:
                self.raiz = nodo
            self.cuantos +=1
        else:
            if elemento== nodo.elemento:
                print("El elemento ya se encuentra en el arbol")
            elif elemento < nodo.elemento:
                nodo.izquierdo= self.aux_agregar(elemento,nodo.izquierdo)
            elif elemento > nodo.elemento:
                nodo.derecho=self.aux_agregar(elemento,nodo.derecho)
        
        return nodo
            
    def eliminar(self,elemento):
        self.raiz =  self.aux_eliminar(elemento, self.raiz)
    
    def aux_eliminar(self,elemento,nodo):
        if nodo == None:
            return nodo
        #Buscamos el nodo que contiene el elemento que se desea eliminar
        elif elemento < nodo.elemento:
            nodo.izquierdo = self.aux_eliminar(elemento, nodo.izquierdo)
        elif elemento > nodo.elemento:
            nodo.derecho = self.aux_eliminar(elemento, nodo.derecho)
        #Caso 1: Si es un Nodo con los dos hijos: izquierdo y derecho
        elif nodo.izquierdo != None and nodo.derecho != None:
            print("Eliminar nodo que no es hoja,,,")
            nodo.elemento = self.aux_minimo(nodo.derecho).elemento
            print("el más pequeño es" ,nodo.elemento)
            nodo.derecho = self.aux_eliminar(nodo.elemento, nodo.derecho)
        else: 
        #Caso 2: 
            nodo = nodo.izquierdo if (nodo.izquierdo!=None) else nodo.derecho
        return nodo
                
 
    def encontrar_minimo(self):
        min = self.aux_minimo(self.raiz);
        print("Minio",min)
        return min
    
    def aux_minimo(self, nodo):
        if nodo == None:
            return None
        elif nodo.izquierdo == None:
            return nodo
        
        return self.aux_minimo(nodo.izquierdo)
        
    
    def encontrar_maximo(self):
        max = self.aux_maximo(self.raiz);
        return max
    
    def aux_maximo(self, nodo):
        if nodo == None:
            return None
        elif nodo.derecho == None:
            return nodo
        return self.aux_maximo(nodo.derecho)
            
    
    def recorrid_preorden(self):
        print("Preorden...")
        if(self.esta_vacio()):
            print("Árbol sin elementos")
        else:
            self.aux_preorden(self.raiz)
        
    def aux_preorden(self, nodo):
        if (nodo!=None):
            print(nodo.__str__())         
            self.aux_preorden(nodo.izquierdo)
            self.aux_preorden(nodo.derecho)
            
        
    def recorrido_inorden(self):
        print("Inorden...")
        if(self.esta_vacio()):
            print("Árbol sin elementos")
        else:
            self.aux_inorden(self.raiz)       
    
    def aux_inorden(self, nodo):
         if (nodo!=None):            
            self.aux_inorden(nodo.izquierdo)
            print(nodo.__str__())
            self.aux_inorden(nodo.derecho)
    
    def recorrido_postorden(self):
        print("Postorden...")
        if(self.esta_vacio()):
            print("Árbol sin elementos")
        else:
            self.aux_postorden(self.raiz)   
    
    def aux_postorden(self,nodo):
        if (nodo!=None):
            self.aux_postorden(nodo.izquierdo)
            self.aux_postorden(nodo.derecho)
            print(nodo.__str__())
        
   
    def contiene(self,elemento):
        return self.aux_contiene(elemento, self.raiz)
    
    def aux_contiene(self,elemento,nodo):
        if nodo == None:
            return False
        else:
            if elemento < nodo.elemento:
                return self.aux_contiene(elemento,nodo.izquierdo)
            elif elemento > nodo.elemento:
                return self.aux_contiene(elemento,nodo.derecho)
            else:
                return True
            
            