# -*- coding: utf-8 -*-

"""
Clase Nodo que representa las cajas donde se 
guarda cada elemento del árbol
"""
class Nodo:
    def __init__(self, elemento=None, izquierdo=None,derecho=None):
        self.elemento = elemento
        self.izquierdo = izquierdo
        self.derecho = derecho
        
    def __str__(self):
        return str(self.elemento)