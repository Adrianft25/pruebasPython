''' EJERCICIO 4 NÚMEROS PRIMOS

Escribe un programa que se encargue de comprobar si un número es primo o no.
Imprime los números primos entre 1 y 100.

'''

def num_primos():
    for i in range(1,101):
        if i >= 2:
           
            divisible = False

            for j in range(2, i):
                if i % j == 0:
                    divisible = True
                    break
            
            if not divisible:
                print(i)

num_primos()