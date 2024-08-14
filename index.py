
# IMPORTAR LAS FUNCIONES AL INDEX PARA SER USADAS 

from funciones.Luke_Skywalker import info_luke
from funciones.c_3po import info_c_3po
from funciones.r2_d2 import info_r2_d2
from funciones.Darth_Vader import info_darth
from funciones.Leia_Organa import info_leia
from funciones.Owen_Lars import info_owen
from funciones.Beru_Whitesun import info_beru
from funciones.r5_d4 import info_r5
from funciones.Biggs_Darklighter import info_biggs
from funciones.Obi_Wan import info_obi
from funciones.personajes_completos import personajes_completos



while True:

    # MENU DE ENTRADA PARA EL USUARIO, PARA OBTENER INFORMACION DEL PERSONAJE EN UN ARCHIVO JSON

    print("""
          Enciclopedia Star Wars
          1.  informacion de Luke Skywalker.
          2.  informacion de C-3PO.
          3.  informacion de R2-D2.
          4.  informacion de Darth Vader.
          5.  informacion de Leia Organa.
          6.  informacion de Owen Lars.
          7.  informacion de Beru Whitesun lars.
          8.  informacion de R5-D4.
          9.  informacion de Biggs Darklighter
          10. informacion de Obi-Wan Kenobi
          11. personajes completos.
          12. salir,
          """)
    try:

        # ENTRADA DE USUARIO

        usuario = int(input("Ingresa una opcion: "))

        # FUNCIONES IMPORTADAS AL INDEX 

        if usuario == 1:
            info_luke()
        elif usuario == 2:
            info_c_3po()
        elif usuario == 3:
            info_r2_d2()
        elif usuario == 4:
            info_darth()
        elif usuario == 5:
            info_leia()
        elif usuario == 6:
            info_owen()
        elif usuario == 7:
            info_beru()
        elif usuario == 8:
            info_r5()
        elif usuario == 9:
            info_biggs()
        elif usuario == 10:
            info_obi()
        elif usuario == 11:
            personajes_completos()
        elif usuario == 12:

            # MENSAJE DE SALIDA 

            print("Hasta la proxima.")
            break
    
    # MANEJOR DE ERRORES 

    except ValueError:
        print("Error de digitacion, vuelve a intentar.")
    