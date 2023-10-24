
# -*- coding: utf-8 -*-
from ApilableAbstract import Apilable
from Nodo import Nodo

"""
Se implementa la clase Pila
"""
class Pila(Apilable):
    
    
    def __init__(self):
        self.tope = None
        self.cuantos = 0

    def esta_vacia(self):
        return self.cuantos == 0
    def vaciar(self):
        self.tope = None
        self.cuantos = 0
    def top(self):
        return self.tope.elemento if not(self.esta_vacia()) else None
    
    def pop(self):
        if (self.esta_vacia()):
            return None
        
        dato = self.tope.elemento
        self.tope = self.tope.siguiente
        self.cuantos-=1        
        return dato
    
    def push(self, elemento):
        nuevo = Nodo(elemento, self.tope)
        self.tope =  nuevo
        self.cuantos+=1
    
    def tamanio(self):
        return self.cuantos
              
    def imprimir(self):
            it = self.iterador()
            print("Imprimir...")
            while (it.has_next()):
                print(it.next())
     
    def iterador(self):
         return _Iterador(self.tope)
"""
Clase privada para implementar un iterador que permita
recorrer los elementos de la pila
"""    
class _Iterador:
    
    def __init__(self, tope):    
        self.posicion = tope
        
    def has_next(self):
        return self.posicion!= None
    
    def next(self):
        if self.posicion == None:
            raise NameError("Se llegó al final de la lista")
                                
        elemento = self.posicion.elemento
        self.posicion = self.posicion.siguiente
            
        return elemento
    