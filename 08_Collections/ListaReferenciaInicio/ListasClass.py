


# -*- coding: utf-8 -*-

"""
 Clase abstracta para implementar una lista simplemente ligada
 Objetivo: Analizar su implementación y complejidad.
 @author Jess
 @version 1.0
"""
from  ListasLigadasAbstract import ListaLigadasAbstract
from Nodo import Nodo

        
class ListaClass(ListaLigadasAbstract):
    
    def __init__(self):
        self.inicio = None
        self.cuantos = 0
        
    def esta_vacia(self):
        return self.cuantos == 0
    
    def vaciar(self):
        self.inicio = None
        self.cuantos = 0

    def agregar(self,elemento):
        nuevo = Nodo(elemento, self.inicio)
        self.inicio = nuevo
        self.cuantos+=1



    def contiene(self,elemento):
       if(not self.esta_vacia()):
           posicion = self.inicio
           while(posicion!=None and 
                 (not posicion.elemento == elemento)):
               posicion = posicion.siguiente
           return posicion != None
       return False
   
    def repeticiones(self,elemento):
       cuantos = 0
       if(not self.esta_vacia()):
           posicion = self.inicio
           while(posicion!=None):
               if (posicion.elemento == elemento):
                   cuantos += 1
               posicion = posicion.siguiente
       return cuantos
           
    
    def primer_elemento(self):
        if(not self.esta_vacia()):
              return self.inicio.elemento
        raise NameError("Lista sin elementos")
          
    
    def eliminar(self,elemento):
        pos = self.inicio
        anterior = None
        while (pos!=None and ( pos.elemento!=elemento)):
            #print("****",pos.elemento)
            anterior = pos
            pos = pos.siguiente
            #print("****",self.inicio.elemento)
        if  pos != None:
            if pos.elemento == self.inicio.elemento:
                   self.inicio = self.inicio.siguiente
                   print("inicio:",self.inicio)
            else:
                   anterior.siguiente = pos.siguiente
            self.cuantos -=1

    def sustituir(self,actual,nuevo):
        posicion = self.inicio
        while (posicion != None):
            if posicion.elemento == actual:
                posicion.elemento = nuevo
            posicion = posicion.siguiente
      
    def imprimir(self):
            it = self.iterador()
            print("Imprimir...")
            while (it.has_next()):
                print(it.next())
     
    def iterador(self):
         return _Iterador(self.inicio)



class _Iterador:
    def __init__(self, inicio):    
        self.posicion = inicio
        
    def has_next(self):
        return self.posicion!= None
    def next(self):
        if self.posicion == None:
            raise NameError("Se llegó al final de la lista")
                                
        elemento = self.posicion.elemento
        self.posicion = self.posicion.siguiente
            
        return elemento
    
    
    