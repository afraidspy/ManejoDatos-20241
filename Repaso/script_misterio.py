# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

def misterioso(matriz):
    for i in matriz:
        print(i)
    num_filas = len(matriz)
    count_filas = 0
    count_cols = num_filas - 1
    
    sum1 = 0
    sum2 = 0

    for i in range(num_filas):
        #print(countFilas,",",countCols)
        sum2 += matriz[count_filas][count_cols]
        for j in range(len(matriz[i])):
            if i==j:
                sum1 += matriz[i][j]          
        count_filas +=1
        count_cols -=1
    
    #for i in range(num_filas):
    #    sum1 += matriz[i][i]          
    #    sum2 += matriz[i][num_filas - 1 - i]

        
        

    resultado = math.fabs(sum1 - sum2)
    print("Resultado: ", resultado)
          
if __name__ == '__main__':
    matriz = [[1,2,3],[4,5,6],[9,8,9]]
    misterioso(matriz)