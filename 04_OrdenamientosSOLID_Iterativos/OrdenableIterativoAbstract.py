
"""
 Clase abstracta para implementar diferentes tipos de ordenamientos
 Los elementos se ordenarán de MENOR A MAYOR
 Objetivo: Analizar su implementación y complejidad.
 @author Jess
 @version 1.0
"""
from abc import ABC, abstractmethod

class OrdenableIterativoAbstractClass(ABC):
   @abstractmethod
   def ordenar(elementos):
       pass
   """
       Intercambia el elemento de la posición i por el de j y viceversa
       
   """
   def intercambiar(self, elementos, i, j):
       aux = elementos[i]
       elementos[i] = elementos[j]
       elementos[j] = aux