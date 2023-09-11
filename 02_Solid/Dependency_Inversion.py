'''
The Dependency Inversion Principle (DIP)
“Abstractions should not depend on details.
Details should depend on abstraction.
High-level modules should not depend on low-level modules.
Both should depend on abstractions”
'''

class Articulo:
    def __init__(self, id, nombre, precio):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def set_id(self,id_nuevo):
        self.__id = id_nuevo

    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_precio(self,nuevo_precio):
        self.__id = id_nuevo

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f"{self.__id},{self.__nombre},{self.__precio}"

class Usuario:
    def __init__(self, id, nombre, lista):
        self.__id = id
        self.__nombre = nombre
        self.__lista = lista

    def set_id(self, nuevo_id):
        self.__id = nuevo_id
        
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_lista_articulos(self, nueva_lista):
        self.__lista = nueva_lista

    def get_lista(self):
        return self.__lista

    def get_nombre(self):
        return __nombre

    def __str__(self):
        return f"Nombre {self.__nombre}"

    
class CarritoCompras:

    def __init__(self, usuario):
        self.__usuario = usuario


    def guardar_articulos(self):
        for art in self.__usuario.get_lista():
            file =  File()
            file.guardar_articulo(art)

class File:

    def guardar_articulo(self,articulo):
       try:
            with open('info_articulos.csv','a',encoding = 'utf-8') as f:
                        print(articulo)
                        f.write(articulo.__str__()+"\n")
       except FileNotFoundError:
                print("Archivo no encontrado")
    

user = Usuario(1,"Lola",[Articulo(1,"Computadora",20000),
                         Articulo(2,"iphone",32000)])

carrito = CarritoCompras(user)

carrito.guardar_articulos()
