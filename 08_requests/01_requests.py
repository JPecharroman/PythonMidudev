# Requests en Python
    
# Requests es una libreria que nos permite hacer peticiones a una API
# Lo haremos con y sin dependencias

# 1. Sin dependencias, solo modulos nativos de Python
import urllib.request # Modulo para hacer peticiones HTTP
import json # Modulo para parsear JSON, sirve para convertir JSON a Python y viceversa

from os import system
system("cls")

url = "https://jsonplaceholder.typicode.com/posts/1"

response = urllib.request.urlopen(url) # Va a esta url pasada por parametro y la abre
# response.read() # Lee la respuesta
# response.getheaders() # Obtiene los headers
# response.getcode() # Obtiene el codigo de estado
datos = response.read() # Lee la respuesta, estos datos vienen en formato binario, no son legibles por el usuario
json_datos = json.loads(datos.decode("utf-8")) # Los pasamos a formato JSON, .decode("utf-8") es para que los datos sean legibles
print(json_datos)

# Al finalizar la peticion, cerramos la conexion
response.close()

# Lo normal es hacer las peticiones con un try except
try:
    url = "https://jsonplaceholder.typicode.com/posts/2"
    response = urllib.request.urlopen(url)
    datos = response.read()
    json_datos = json.loads(datos.decode("utf-8"))
    print(json_datos)
except urllib.error.HTTPError as e: # Error HTTP
    print(f"Error HTTP: {e}")
except urllib.error.URLError as e: # Error URL
    print(f"Error en la solicitud URL: {e}")
except Exception as e: # Error General
    print(f"Error General: {e}")
finally:
    response.close()


# 2. Con dependencias, requests
# Requests es una libreria que nos permite hacer peticiones a una API
# Debemos importarla, pero no es nativa de Python, se debe instalar con pip
# pip install requests o pip3 install requests
import requests

system("cls")

# GET
url = "https://jsonplaceholder.typicode.com/posts"
print("\nGET:")
response = requests.get(url)
# print(response.status_code)
json = response.json()
print("JSON:")
print(json[0]) # json[0] es para acceder al primer elemento del array
print()
texto = response.text
print("Texto:")
print(texto) # texto es para acceder a los datos en formato string

# POST
print("\nPOST:")
datos = {"title": "foo", "body": "bar", "userId": 5}
response = requests.post(url, json=datos)
json = response.json() # Nos devuelve la respuesta, si todo ha ido bien, en formato JSON
print(json)

# Con response() podemos acceder a la respuesta de la peticion, entre otras cosas podemos mirar el status code de la peticion
print("\nStatus code:")
print(response.status_code)
# Si nos devuelve 200, o 201 todo ha ido bien. Si hay algun problema devolvera un codigo de error

# Gracias a status podemos manejar los errores con try except
url_mala = "https://jsonplaceholder.typicode.c"
try:
    response = requests.get(url_mala)
    response.raise_for_status() # Si el status code es mayor o igual a 400, lanza una excepcion
except requests.exceptions.HTTPError as e: # Error HTTP
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e: # Error de conexion
    print(f"Error de conexion: {e}")
except requests.exceptions.Timeout as e: # Error de timeout
    print(f"Error de timeout: {e}")
except requests.exceptions.RequestException as e: # Error general
    print(f"Error general: {e}")
finally:
    response.close()

# PUT
# El PUT se usa para actualizar un recurso, debemos indicarle a que parte debemos acceder para modificarla
system("cls")
print("\nPUT:")
url = "https://jsonplaceholder.typicode.com/posts/"
try:
    response = requests.put(url, json={"title": "foo", "body": "bar", "userId": 5, "id": 1})
    json = response.json()
    print(json)
    print(response.status_code) # Nos devuelve el status code de la peticion, 404 significa que no se ha encontrado la id pasada, debemos ir directamente desde url
    response = requests.put(url + "1", json={"title": "foo", "body": "bar", "userId": 5})
    print(response.json())
    print(response.status_code) # Nos devuelve el status code de la peticion, 200 significa que todo ha ido bien
except requests.exceptions.HTTPError as e: # Error HTTP
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e: # Error de conexion
    print(f"Error de conexion: {e}")
except requests.exceptions.Timeout as e: # Error de timeout
    print(f"Error de timeout: {e}")
except requests.exceptions.RequestException as e: # Error general
    print(f"Error general: {e}")
finally:
    response.close()

# PATCH
# El PATCH se usa para actualizar un recurso, su diferencia con PUT es que solo actualiza los campos que le indiquemos, no debemos pasarle todos los campos

print("\nPATCH:")
url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.patch(url, json={"title": "foo", "body": "bar", "userId": 5})
    json = response.json()
    print("JSON:")
    print(  json)
    print("Status code:")
    print(response.status_code) # Nos devuelve el status code de la peticion, 200 significa que todo ha ido bien
except requests.exceptions.HTTPError as e: # Error HTTP
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e: # Error de conexion
    print(f"Error de conexion: {e}")
except requests.exceptions.Timeout as e: # Error de timeout
    print(f"Error de timeout: {e}")
except requests.exceptions.RequestException as e: # Error general
    print(f"Error general: {e}")
finally:
    response.close()

# DELETE
# El DELETE se usa para eliminar un recurso

print("\nDELETE:")
url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.delete(url)
    json = response.json()
    print("JSON:")
    print(json)
    print("Status code:")
    print(response.status_code) # Nos devuelve el status code de la peticion, 200 significa que todo ha ido bien
except requests.exceptions.HTTPError as e: # Error HTTP
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e: # Error de conexion
    print(f"Error de conexion: {e}")
except requests.exceptions.Timeout as e: # Error de timeout
    print(f"Error de timeout: {e}")
except requests.exceptions.RequestException as e: # Error general
    print(f"Error general: {e}")
finally:
    response.close()
