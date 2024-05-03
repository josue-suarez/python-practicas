# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def funcion(ls_string1, ls_string2):
    ln_acumulador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(ls_string1 + ls_string2)
            ln_acumulador += 1
        elif i % 3 == 0:
            print(ls_string1)
            ln_acumulador += 1
        elif i % 5 == 0:
            print(ls_string2)
            ln_acumulador += 1
    return ln_acumulador

def main():
    gs_texto1 = input("Introduzca texto a:")
    gs_texto2 = input("Introduzca texto b:")
    gn_acumulador = funcion(gs_texto1, gs_texto2)
    print("Número de veces impreso:", gn_acumulador)

if __name__ == "__main__":
    main()

