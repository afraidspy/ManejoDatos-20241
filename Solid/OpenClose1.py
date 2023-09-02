# -*- coding: utf-8 -*-
"""
Open and Closed Principle(OCP):
Software entities (classes, function, module) open for extension, but not for modification (or closed for modification)
@author: guest
"""

class Usuario:
    
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo =  tipo
        
        
    def calcular_total(self,lista_articulos):
        total = 0
        for i in lista_articulos:
            total+= i
            
        for i in lista_articulos:
            if self.__tipo =="nivel0":
                return total
            elif self.__tipo == "nivel1":
                return total - total * 0.01
            elif self.__tipo == "nivel2":
                return total - total * 0.03
            elif self.__tipo == "nivel3":
                return total - total * 0.05
            
        
        """match tipo:
            case "nivel":
                return total
            case "nivel":
                return total
            case "nivel":
                return total
        """    
            

if __name__ == "__main__":
   user = Usuario("Juana","nivel1")
   
   total = user.calcular_total([25.0,45.0,32.50])     
   
   print("Total: ", total )
    
                 
                
                
                
