
# IMPORTAR LA LIBRERIA "REQUEST" PARA REALIZAR PETICIONES "HTTP" A LA API

import requests

# DEFINIR UNA FUNION PARA USARLA EN EL INDEX

def info_r5():

    # LLAMADO A LA "API" CON LA INFORMACION DEL OCTAVO PERSONAJE

    url = "https://swapi.dev/api/people/8"

    # CON EL MODULO "GET" DEVUELVE EL VALOR DE LA URL DE KA "API"

    respuesta = requests.get(url)

    # CONVERTIR LA RESPUESTA A UN ARCHIVO JSOM

    peticion_json = respuesta.json()

    # ITERAR EN EL ARCHIVO JSON 

    for personaje in peticion_json.items():

        # SE MUESTRA EL RESULTADO
        
        print(personaje) 