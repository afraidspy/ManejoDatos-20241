# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 07:30:31 2023

@author: guest
"""

from abc import ABC, abstractmethod

class EncolableAbstract:
    @abstractmethod
    def esta_vacia():
        pass
    @abstractmethod
    def vaciar():
        pass
    @abstractmethod
    def agregar(elemento):
        pass
    @abstractmethod
    def contiene(elemento):
        pass
    @abstractmethod
    def tomar():
        pass
    @abstractmethod
    def primer_elemento():
        pass
    @abstractmethod
    def eliminar(eliminar):
        pass
    @abstractmethod
    def imprimir():
        pass
    @abstractmethod
    def iterador():
        pass
    

        