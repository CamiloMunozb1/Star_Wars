import requests

def info_beru():
    url = "https://swapi.dev/api/people/7"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 