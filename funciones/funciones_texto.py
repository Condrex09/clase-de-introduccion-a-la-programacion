nombre = "Benjamin"
apellido = "Gomez"
nombre_completo = nombre + " " + apellido
#nombre y apellido en mayusculas
nombre_mayusculas = nombre.upper()
apellido_mayusculas = apellido.upper()
#nombre y apellido en minusculas
nombre_minusculas = nombre_mayusculas.lower()
apellido_minusculas = apellido_mayusculas.lower()
#nombre y apellido en titulo
nombre_titulo = nombre.title()
apellido_titulo = apellido.title()

print(nombre_completo.endswith("a"))

print(f"hola admirable y mayusculas {nombre} {apellido} {3+4}")
print(f"nombre y apellido en mayusculas: {nombre_mayusculas} {apellido_mayusculas}")
print(f"nombre y apellido en minusculas: {nombre_minusculas} {apellido_minusculas}")
print(f"nombre y apellido en titulo: {nombre_titulo} {apellido_titulo}")