
miListaOriginal = [0,1,2,3,4,5,6,7]
print(miListaOriginal)

miLista = [i for i in range(len(miListaOriginal))]
print(miLista)

miLista = [i for i in miListaOriginal]
print(miLista)

miLista = [i+1 for i in miListaOriginal]
print(miLista)

miLista = [i*2 for i in miListaOriginal]
print(miLista)

miLista = [i*i for i in miListaOriginal]
print(miLista)

def sum_cinco(number):
    return number + 5

miLista = [sum_cinco(i) for i in miListaOriginal]
print(miLista)