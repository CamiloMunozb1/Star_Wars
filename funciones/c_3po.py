import requests

def info_c_3po():
    url = "https://swapi.dev/api/people/2"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje)