"""
Clase Nodo que representa las cajas donde se 
guarda cada elemento de la pila
"""
class Nodo:
    def __init__(self, elemento=None, siguiente=None):
        self.elemento = elemento
        self.siguiente = siguiente
        
    def __str__(self):
        return str(self.elemento)# -*- coding: utf-8 -*-

