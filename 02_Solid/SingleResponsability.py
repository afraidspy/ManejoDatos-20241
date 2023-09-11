# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:28:21 2022

@author: Jessica

A class should have one, and only one, reason to change
"""
class CalculosNumericos:
    
    def __init__(self,lista=[2,3,3,7,9]):
        self.list = lista
        dic_moda = {}
        sum = 0
        for i in range(len(self.list)):
            sum+= self.list[i]
            cve = str(lista[i])
            if not cve in dic_moda:
                dic_moda[cve] = 1
            else:
                dic_moda[cve] +=1
        mas_frecuente = dic_moda['2']
        cve_mas_freq = '2'
        for k in dic_moda:
            if mas_frecuente < dic_moda[k]:
                mas_frecuente = dic_moda[k]
                cve_mas_freq = k
        print("resultado: ",cve_mas_freq)
        print("resultado2: ", sum / len(self.list))
                
  

if __name__ == "__main__":
    calc =  CalculosNumericos()
        
    
    
