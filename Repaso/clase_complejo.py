class NumeroComplejo:
    def __init__(self, parte_real, parte_imaginaria):
        self._parte_real = parte_real
        self._parte_imaginaria = parte_imaginaria

    def obtener_parte_real(self):
        return self._parte_real

    def obtener_parte_imaginaria(self):
        return self._parte_imaginaria

    def sumar(self, otro_complejo):
        nueva_parte_real = self._parte_real + 
        otro_complejo.obtener_parte_real()
        
        nueva_parte_imaginaria = self._parte_imaginaria + 
        otro_complejo.obtener_parte_imaginaria()
        
        return NumeroComplejo(nueva_parte_real, nueva_parte_imaginaria)

    def restar(self, otro_complejo):
        nueva_parte_real = self._parte_real - otro_complejo.obtener_parte_real()
        nueva_parte_imaginaria = self._parte_imaginaria - otro_complejo.obtener_parte_imaginaria()
        return NumeroComplejo(nueva_parte_real, nueva_parte_imaginaria)

    def __str__(self):
        if self._parte_imaginaria >= 0:
            return f"{self._parte_real} + {self._parte_imaginaria}i"
        else:
            return f"{self._parte_real} - {abs(self._parte_imaginaria)}i"

# Crear dos instancias de NumeroComplejo
complejo1 = NumeroComplejo(3, -2)
complejo2 = NumeroComplejo(1, 4)

# Sumar y restar los números complejos
resultado_suma = complejo1.sumar(complejo2)
resultado_resta = complejo1.restar(complejo2)

# Mostrar los resultados
print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)