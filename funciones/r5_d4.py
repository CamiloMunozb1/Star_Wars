import requests

def info_r5():
    url = "https://swapi.dev/api/people/8"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 