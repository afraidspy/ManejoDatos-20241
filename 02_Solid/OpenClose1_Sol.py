# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:20:09 2023

@author: guest
"""

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre

    def calcular_total(self, lista_articulos):
        total = sum(lista_articulos)
        return total


class UsuarioNivel0(Usuario):
    def calcular_total(self, lista_articulos):
        return super().calcular_total(lista_articulos)

class UsuarioNivel1(Usuario):
    def calcular_total(self, lista_articulos):
        total = super().calcular_total(lista_articulos)
        return total - total * 0.01


class UsuarioNivel2(Usuario):
    def calcular_total(self, lista_articulos):
        total = super().calcular_total(lista_articulos)
        return total - total * 0.03


class UsuarioNivel3(Usuario):
    def calcular_total(self, lista_articulos):
        total = super().calcular_total(lista_articulos)
        return total - total * 0.05
