import requests

def info_luke():
    url = "https://swapi.dev/api/people/1"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 