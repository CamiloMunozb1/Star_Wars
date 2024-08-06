
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
            print("Proxima funcionalidad.")
        elif usuario == 2:
            print("Proxima funcionalidad.")
        elif usuario == 3:
            print("Muchas gracias por visitarnos.")
            break
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")
    