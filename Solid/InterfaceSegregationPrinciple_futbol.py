# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:37:10 2023

@author: guest
"""

from abc import ABC, abstractmethod

class JugadorDeFutbol(ABC):
    @abstractmethod
    def correr(self):
        pass

    @abstractmethod
    def pasar_pelota(self):
        pass

    @abstractmethod
    def defender(self):
        pass

    @abstractmethod
    def celebrar_gol(self):
        pass

    @abstractmethod
    def dar_un_pase_largo(self):
        pass

class Delantero(JugadorDeFutbol):
    def correr(self):
        print("Delantero corre velozmente.")

    def pasar_pelota(self):
        print("Delantero realiza un pase corto.")


    def celebrar_gol(self):
        print("Delantero celebra un gol.")

    def dar_un_pase_largo(self):
        print("Delantero realiza un pase largo.")

class Portero(JugadorDeFutbol):
    def correr(self):
        print("Portero se mueve dentro del área.")

    def defender(self):
        print("Portero se lanza para atajar el balón.")

