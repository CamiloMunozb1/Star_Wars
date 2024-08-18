
# IMPORTAR LA LIBRERIA "REQUEST" PARA REALIZAR PETICIONES "HTTP" A LA API

import requests

# DEFINIR UNA FUNION PARA USARLA EN EL INDEX

def personajes_completos():

    # LLAMADO A LA "API"

    url = "https://swapi.dev/api/people"

    # CON EL MODULO "GET" DEVUELVE EL VALOR DE LA URL DE KA "API"

    respuesta = requests.get(url)

    # CONVERTIR LA RESPUESTA A UN ARCHIVO JSOM

    peticion_json = respuesta.json()["results"]

    # ITERAR EN EL ARCHIVO JSON 

    for personajes in peticion_json:

        # SE MUESTRA EL RESULTADO
        
        print(personajes["name"])