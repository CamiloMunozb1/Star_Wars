from funciones.info_personajes import info_personajes
from funciones.personajes_completos import personajes_completos
while True:
    print("""
          Enciclopedia Star Wars
          1. Buscar personajes.
          2. Mostrar personajes.
          3. Salir.
          """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            info_personajes()
        elif usuario == 2:
            personajes_completos()
        elif usuario == 3:
            print("Muchas gracias por visitarnos.")
            break
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")
    