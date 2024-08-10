import requests

def info_obi():
    url = "https://swapi.dev/api/people/10"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 