# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:32:22 2023

@author: guest
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_informacion(self):
        return f"{self.titulo} por {self.autor}"

class LibroImpreso(Libro):
    def __init__(self, titulo, autor, numero_de_paginas):
        super().__init__(titulo, autor)
        self.numero_de_paginas = numero_de_paginas

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, {self.numero_de_paginas} páginas impresas"

class LibroElectronico(Libro):
    def __init__(self, titulo, autor, tamano_en_mb):
        super().__init__(titulo, autor)
        self.tamano_en_mb = tamano_en_mb

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, {self.tamano_en_mb} MB en formato electrónico"


def mostrar_informacion_libro(libro:Libro):
    print(libro.obtener_informacion())
