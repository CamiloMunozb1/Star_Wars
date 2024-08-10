import requests

def info_r2_d2():
    url = "https://swapi.dev/api/people/3"
    respuesta = requests.get(url)
    peticion_json = respuesta.json()
    for personaje in peticion_json.items():
        print(personaje) 