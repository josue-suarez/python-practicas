# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización
#   y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#   y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más
#   de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.




def main():
    print("AGENDA DE CONTACTOS")
    int(input("""Elija una opción:
          1. Buscar contacto
          2. Nuevo contacto
          3. Borrar contacto
          Ingrese opción: """))
    

if __name__ == "__main__":
    main()
