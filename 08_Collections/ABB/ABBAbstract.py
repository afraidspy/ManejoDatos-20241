"""
 Clase abstracta para implementar una ABB
 Objetivo: Analizar su implementación y complejidad.
 @author Jess
 @version 1.0
"""

from abc import ABC, abstractmethod

class ArbolBuscable(ABC):
    @abstractmethod
    def esta_vacio(self):
        pass
    @abstractmethod
    def vaciar(self):
        pass
    @abstractmethod
    def tamanio(self):
        pass
    @abstractmethod
    def agregar(self):
        pass
    @abstractmethod
    def eliminar(self,elemento):
        pass
    @abstractmethod
    def encontrar_minimo(self):
        pass
    @abstractmethod
    def encontrar_maximo(self):
        pass
    @abstractmethod
    def recorrid_preorden(self):
        pass
    @abstractmethod
    def recorrido_inorden(self):
        pass
    @abstractmethod
    def recorrido_postorden(self):
        pass
    @abstractmethod
    def contiene(self,elemento):
        pass
    
     
