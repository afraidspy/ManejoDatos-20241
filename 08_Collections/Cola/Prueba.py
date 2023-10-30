from Cola import ColaClass


cola = ColaClass()

print("¿La cola está vacía?", cola.esta_vacia())

cola.agregar(1)
cola.agregar(2)
cola.agregar(3)

print("¿La cola contiene el elemento 2?", cola.contiene(2))

cola.imprimir()


print ("Eliminamos el primer elemento de la cola:"), cola.eliminar()

cola.imprimir()

print("Tomar un elemento de la cola:", cola.tomar())

cola.imprimir()

cola.vaciar()

print("¿La cola está vacía?", cola.esta_vacia())