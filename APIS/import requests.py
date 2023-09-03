import requests
import json

# Definir la URL de la API de GitHub y el nombre de usuario
api_url = "https://api.github.com"
username = "nombre_de_usuario"

# Realizar una solicitud GET a la API para obtener información del usuario
response = requests.get(f"{api_url}/users/{username}/repos")

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    repos = json.loads(response.text)

    # Imprimir información sobre los repositorios
    for repo in repos:
        print(f"Nombre del repositorio: {repo['name']}")
        print(f"Descripción: {repo['description']}")
        print(f"URL del repositorio: {repo['html_url']}")
        print()
else:
    print(f"Error al realizar la solicitud: Código de estado {response.status_code}")

