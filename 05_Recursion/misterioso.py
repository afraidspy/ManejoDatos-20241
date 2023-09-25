# -*- coding: utf-8 -*-
"""


@author: guest
"""

def misterioso(n, k):
    print("n:", n)
    if n > 1:
        return k + misterioso(n - 1, k)
    else:
        return k

if __name__ == "__main__":
    
    n = int(input("Ingrese el valor de n: "))
    k = int(input("Ingrese el valor de k: "))
    result = misterioso(n, k)
    print("Resultado:", result)


