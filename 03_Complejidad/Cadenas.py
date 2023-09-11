# -*- coding: utf-8 -*-

class Algoritmos:
    
    def __init__(self, cadena):
        self.__cadena =  cadena
    
    
    def set_cadena(self, cadena):
        self.__cadena = cadena
    
    def get_cadena(self):
        return self.__cadena
    
    
    def hay_repeticiones(self):
        if (self.__cadena == None):
            return
        tam_cad = len(self.__cadena)
        if (tam_cad < 2):
            print("Sin repeticiones")
        
        indice = tam_cad - 1
        for elemento in self.__cadena:
            print("Caracter-inicio" , elemento)
            print("Caracter-fin" , self.__cadena[indice])
            if(elemento==self.__cadena[indice]):
                print("Contiene caráceres iguales")
                break
            indice -=1
            

                

algoritmo = Algoritmos("Pedro")

algoritmo.hay_repeticiones();

        
        
        
