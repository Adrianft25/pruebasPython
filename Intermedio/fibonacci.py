''' EJERCICIO 3 SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie de Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores:
    0,1,1,2,3,5,8,13...

'''

def fibonacci():

    n1 = 0
    n2 = 1

    for i in range(0, 50):
        print(i, ":", n1)

        fib = n2 + n1
        n1 = n2
        n2 = fib


fibonacci()