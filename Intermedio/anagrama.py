''' EJERCICIO 2 ANAGRAMAS

Escribe una función que reciba dos palabras (strings) y retorne verdadero o falso (boolean) según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagramas.

'''
def anagrama(string1, string2):

    if string1.lower() == string2.lower():
        return False
    elif sorted(string1.lower()) == sorted(string2.lower()):
        return True
    elif sorted(string1.lower()) != sorted(string2.lower()):
        return False

print(anagrama("amor", "amor"))
print(anagrama("rOma", "AmoR"))
print(anagrama("asdf", "amor"))