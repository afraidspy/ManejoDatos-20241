# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:32:06 2023

@author: guest
"""

from Cola import ColaAbstract
from Nodo import Nodo

        
class ColaClass(ColaAbstract):
    
    def __init__(self):
        self.inicio =  None
        self.fin = None
        self.cuantos = 0
    
    def esta_vacia(self):
        return self.cuanto == 0
    
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
        
        
            
            
            
                    
    
    