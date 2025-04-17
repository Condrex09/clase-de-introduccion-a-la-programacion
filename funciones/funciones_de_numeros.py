import math
numeros = [2,4,6,8,10,12]
decimal = 12.3456

print(f"el numero mayor a la lista {numeros} es {max(numeros)}")
print(f"el numero menor a la lista {numeros} es {min(numeros)}")

print(f"redondear el decimal {decimal} = {round(decimal)}")
print(f"redondear el decimal {decimal} a 2 decimales = {round(decimal,2)}")
print(f"truncar el decimal {decimal} = {math.trunc(decimal)}")
print(f"valor absoluto de -45 = {math.fabs(45)}")
print(f"Raiz cuadrada de 25 = {math.sqrt(25)}")
print(f"Sumatoria de los numeros {numeros} = {math.fsum(numeros)}")