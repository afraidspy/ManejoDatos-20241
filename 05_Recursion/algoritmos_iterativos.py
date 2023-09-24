def factorial(num):
        if num <= 1:
            return 1
        else:
            resultado = 1
            for i in range(num,0,-1):
                resultado *= i
            
            return resultado
    
    
if  __name__ == "__main__":
    resultado_fact = factorial(5)

    print(resultado_fact)
    
    
    
    