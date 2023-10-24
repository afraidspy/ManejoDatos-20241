# -*- coding: utf-8 -*-

from PilaClass import Pila


pila_nums = Pila()

pila_nums.imprimir()

pila_nums.push(2)
pila_nums.push(1)
pila_nums.push(4)
pila_nums.push(5)

pila_nums.imprimir()

print("Tope",pila_nums.top())
pila_nums.pop()
pila_nums.imprimir()
pila_nums.pop()
pila_nums.imprimir()

pila_nums.push(6)
pila_nums.imprimir()
pila_nums.push(8)
pila_nums.imprimir()

print("Tamaño pila: ",pila_nums.tamanio())


