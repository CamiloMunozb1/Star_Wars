import requests

def personajes_completos():
    url = "https://swapi.dev/api/people"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()["results"]
    for personajes in peticion_json:
        print(personajes["name"])