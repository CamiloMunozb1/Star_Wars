import requests

def info_leia():
    url = "https://swapi.dev/api/people/5"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 