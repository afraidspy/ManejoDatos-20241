# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:08:39 2023

@author: guest
"""


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
    

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_lista(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0,1]
    else:
        return fibonacci(num-1) + fibonacci(num-2)

    
    

if  __name__ == "__main__":
    
    resultado_fact =  factorial(5)
    print(resultado_fact)
    
    resultado_fibo =  fibonacci(5)
    print(resultado_fibo)