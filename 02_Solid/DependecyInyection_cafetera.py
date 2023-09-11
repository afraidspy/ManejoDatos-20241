# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:41:36 2023

@author: guest
"""

class Cafetera:
    def hacer_cafe(self):
        print("preparandoo café")

class Cliente:
    def __init__(self, cafetera):
        self.cafetera = cafetera

    def tomar_cafe(self):
        print("Tomar café")
        self.cafetera.hacer_cafe()