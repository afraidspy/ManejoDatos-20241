# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:01:59 2023

@author: guest
"""

from abc import ABC, abstractmethod
import csv

class LectorCSV(ABC):

    @abstractmethod
    def leer_archivo(self, archivo: str):
        pass

class EscritorCSV(ABC):

    @abstractmethod
    def escribir_archivo(self, archivo: str, datos: list):
        pass

class ArchivoCSV(LectorCSV, EscritorCSV):

    def __init__(self, nombre_archivo: str):
        self.__nombre_archivo = nombre_archivo

    def leer_archivo(self, archivo: str):
        pass

    def escribir_archivo(self, archivo: str, datos: list):
        pass

class GestorArchivos:

    def __init__(self, lector: LectorCSV, escritor: EscritorCSV):
        self.__lector = lector
        self.__escritor = escritor

    def procesar_archivo(self, archivo: str):
        pass