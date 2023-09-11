# -*- coding: utf-8 -*-
"""

@author: guest
"""
class CalculadoraDePrimas:
    def __init__(self):
        self.__factor_auto = 0.03
        self.__factor_motocicleta = 0.06
        self.__factor_camion = 0.09

    def calcular_prima(self, valor_vehiculo, tipo_vehiculo):
        """
        Calcula la prima del seguro para un vehiculo

        Params:
        valor_vehiculo (float)  El valor del vehículo para el cálculo de la prima.
        tipo_vehiculo (str) El tipo de vehículo 

        Return:
        float: La prima calculada para el vehículo.
        """
        if tipo_vehiculo == "auto":
            return valor_vehiculo * self.__factor_auto
        elif tipo_vehiculo == "motocicleta":
            return valor_vehiculo * self.__factor_motocicleta
        elif tipo_vehiculo == "camion":
            return valor_vehiculo * self.__factor_camion

