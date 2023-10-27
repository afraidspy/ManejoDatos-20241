# -*- coding: utf-8 -*-
from ABB import ABB

arbolito = ABB()


arbolito.agregar(5)
arbolito.agregar(8)
arbolito.agregar(10)
arbolito.agregar(7)


arbolito.recorrid_preorden()

arbolito.recorrido_inorden()

arbolito.recorrido_postorden()

##print("Min", arbolito.encontrar_minimo())
##print("Max", arbolito.encontrar_maximo())
##print("Contiene", arbolito.contiene(10))
##print("Contiene", arbolito.contiene(80))


arbolito.eliminar(8)

arbolito.recorrid_preorden()
