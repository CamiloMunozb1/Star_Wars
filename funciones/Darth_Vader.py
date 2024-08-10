import requests

def info_darth():
    url = "https://swapi.dev/api/people/4"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 