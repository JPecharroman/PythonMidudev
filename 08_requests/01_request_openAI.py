# Vamos a usar la API de OpenAI para generar una IA

# Ref: https://platform.openai.com/docs/api-reference/introduction

# Vamos a conectar con la API de OpenAI para generar una IA

import os
os.system("cls")
import requests, json

OPENAI_API_KEY = "API KEY de OpenAI"

def llamar_api_openai(api_key):
    url = "https://api.openai.com/v1/chat/completions"

    # Obtenemos el header de la API
    headers = {
        # Obtenemos la API key de la variable de entorno, bearer es un token de autenticacion que nos da OpenAI y 
        # api_key es la variable de entorno que contiene la API key
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json" # Indicamos que el contenido es JSON
    }

    # Obtenemos el body de la API
    body = {
        "model": "gpt-3.5-turbo", # Indicamos el modelo que vamos a usar
        "messages": [
        {
            "role": "user", # Indicamos que es un usuario
            "content": "Escribe un poema breve sobre la vida" # Indicamos el contenido
        }
    ]
    }

    # Obtenemos la respuesta de la API
    response = requests.post(url, headers=headers, json=body) # Paso de parametros por clave valor, da igual el orden en que los pasemos, headers=headers asignara el header a la peticion
    return response.json()

# Llamamos a la API y guardamos la respuesta en una variable
respuesta_json = llamar_api_openai(OPENAI_API_KEY)
print(json.dumps(respuesta_json, indent=4)) # Indent es para que el JSON sea mas legible, le damos un indent de 4 espacios
print(respuesta_json["choices"][0]["message"]["content"]) # Accedemos al contenido de la respuesta

