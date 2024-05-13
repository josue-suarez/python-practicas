# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización
#   y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#   y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más
#   de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.

def buscar_contacto():

def nuevo_contacto(ls_nombre, ln_telefono):
    print("INTRODUCIR NUEVO CONTACTO")
    ls_nombre = input("Introduzca nombre:")
    ln_telefono = int(input("Introduzca teléfono:"))
    main()

def main():
    dict agenda()
    
    print("AGENDA DE CONTACTOS")
    opcion = int(input("""Elija una opción:
          1. Buscar contacto
          2. Nuevo contacto
          3. Borrar contacto
          4. Salir
          Ingrese opción: """))
    
    if opcion == 1:
        buscar_contacto()
    elif opcion == 2:
        nuevo_contacto()
    elif opcion == 3:
        borrar_contacto()
    elif opcion == 4:
        
    else:
        opcion_incorrecta()
    

if __name__ == "__main__":
    main()
