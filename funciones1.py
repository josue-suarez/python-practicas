# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def funcion(ls_string1, ls_string2):
    for i in 100:
        if i % 3 == 0:
            print(ls_string1)
        elif i % 5 == 0:
            print(ls_string2)
        elif i % 3 == 0 and i % 5 == 0:
            print(ls_string1 + ls_string2)
    return i

def main():
    gs_texto1 = input("Introduzca texto a:")
    gs_texto2 = input("Introduzca texto b:")
    funcion(gs_texto1, gs_texto2)
