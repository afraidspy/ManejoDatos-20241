# -*- coding: utf-8 -*-
"""

@author: guest
"""


def suma_numeros(n):
    """
        Calcula la suma de los primeros n números 

        Params:
        n(int): El númer limite del cual se va a calcular la suma

        Return:
        int: La suma de los primeros n números 
    """
    if n <= 0:
        return 0
    else:
        return n + suma_numeros(n-1)
    
def potencia(base, exp):
    """
        Calcula la potencia de un número base elevado a una potencia exp recursivamente

        Params:
        base(int): El número base.
        exp(int): El exponente al que se elevará el número base.

        Return:
        int: El resultado de elevar la base al exponente exp
    """
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)

def suma_elementos_lista(lista):
    """
    Suma los valores de una lista recursivamente

    Params:
    lista(list): La lista de números 

    Return:
    float: La suma de los elementos de la lista
    """
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_elementos_lista(lista[1:])
    
    
if  __name__ == "__main__":

    print("Suma: " , suma_numeros(4))
    print("Potencia: " , potencia(2, 4))
    print("Suma elementos lista: ",suma_elementos_lista([1,2,0,23]))
    

