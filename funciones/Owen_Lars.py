import requests

def info_owen():
    url = "https://swapi.dev/api/people/6"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 