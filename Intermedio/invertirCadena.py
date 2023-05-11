''' EJERCICIO 5 INVERTIR LA CADENA

Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH".

'''

txt = input("Introduce la cadena que quieres invertir: ")

def reverse(text):

    text = str(text[::-1])
    print(text)

reverse(txt)

txt2 = input("Introduce la cadena que quieres invertir (OTRO MÉTODO): ")

def reverse2(text):
    txt_len = len(text)
    reversed_text = ""
    for i in range(0, txt_len):
        reversed_text += text[txt_len - i - 1]
    return reversed_text

print(reverse2(txt2))