n1, n2 = 5, 1

n2 = "1"

# try except
try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# try except else

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

# try except else finally

try: # Obligatorio
    print(n1 + n2)
    print("No se ha producido un error")
except: # Obligatorio
    print("Se ha producido un error")
else: # Opcional
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(n1 + n2)
    print("No se ha producido un error")
except TypeError: #as e:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion

try:
    print(n1 + n2)
    print("No se ha producido un error")
except Exception as e:
    print(e)
