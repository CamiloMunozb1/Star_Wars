import requests

def info_biggs():
    url = "https://swapi.dev/api/people/9"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 