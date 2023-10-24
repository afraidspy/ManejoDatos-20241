# -*- coding: utf-8 -*-
"""
 Clase abstracta para implementar una pila
 @author Jess
 @version 1.0
"""
from abc import ABC, abstractmethod

class Apilable(ABC):
    @abstractmethod
    def esta_vacia():
        """
        Método para validar si una pila tiene elementos o no
        Returns
        -------
        boolean:True si la pila esta vacía y False en otro caso.
        """
        pass
    @abstractmethod
    def vaciar():
        """
        Método para eliminar a todos los elementos de la pila
        Returns
        -------
        boolean:True si la pila esta vacía y False en otro caso.
        """
        pass
    @abstractmethod
    def top():
        """
        Método para obtener al elemento del tope de la pila.
        Returns
        -------
        elemento - Regresa el último elemento en entrar a la pila.
        """
        pass
    @abstractmethod
    def pop():
        """
        Método para sacar el elemento del tope de la pila-
        -------
        elemento - Regresa el último elemento en entrar a la pila.
        """
        pass
    @abstractmethod
    def push(elemento):
        """
        Método introducir un elemento en el tope de la pila
        Parameters
        ----------
        elemento - el elemento que se desea agregar a la pila
        """
        pass
    @abstractmethod
    def tamanio():
        """
        Método para regresar la cantidad de elementos de la pila
        """
        pass
    @abstractmethod
    def imprimir():
        """
        Método para imprimir llos elementos de una pila
        -------
        elemento - Regresa el último elemento en entrar a la pila.
        """
        pass
    @abstractmethod
    def iterador():
        """
        Método para obtener un iterador sobre la pila
        -------
        Iterador- el objeto iterador de la pila
        """
        pass