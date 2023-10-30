# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:32:06 2023

@author: guest
"""

from Encolable import EncolableAbstract
from Nodo import Nodo

        
class ColaClass(EncolableAbstract):
    
    def __init__(self):
        self.inicio =  None
        self.fin = None
        self.cuantos = 0
    
    def esta_vacia(self):
        return self.cuantos == 0
    
    def vaciar(self):
        self.cuantos = 0
        self.inicio = None
        self.fin = None
    
    def contiene(self,elemento):
        if self.esta_vacia():
            return False
        else:
            posicion =  self.inicio 
            while posicion!=None: 
                if posicion.elemento == elemento:
                    return True
                posicion =  posicion.siguiente
            
            return False
    
    def agregar(self,elemento):
        
        if self.esta_vacia():
            nuevo = Nodo(elemento, None)
            self.inicio = nuevo
            self.fin = nuevo
        
        else:
            nuevo = Nodo(elemento,None)
            self.fin.siguiente = nuevo
            self.fin = nuevo
            
        self.cuantos += 1
    
    def tomar(self):
        if self.esta_vacia():
            return "Sin elementos"
        
        return self.inicio.elemento
    
    def eliminar(self):
        if not self.esta_vacia():
            self.inicio = self.inicio.siguiente
            self.cuantos -=1
            
    def iterador(self):
        return _Iterador(self.inicio)
    
    def imprimir(self):
        it = self.iterador()
        
        while(it.has_next()):
            print(it.next())
        
            

class _Iterador():
    
    def __init__(self, inicio):
        self.posicion =  inicio
        
    def has_next(self):
        return self.posicion != None
    
    def next(self):
        if self.posicion == None:
           raise NameError("Se llegó al final de la lista")
           
        elemento =  self.posicion.elemento
        self.posicion = self.posicion.siguiente
        
        return elemento
        
        
        
    
    
        
        
            
            
            
                    
    
    