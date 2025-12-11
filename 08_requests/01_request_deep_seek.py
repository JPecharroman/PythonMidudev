# Creamos un programa que nos permita buscar en la API de Deepseek
# Deepseek es compatible con OpenAI, por lo que podemos usar casi la misma API que usamos con OpenAI

# Ref: https://deepseek.com/ai-api

import os
os.system("cls")
import requests, json

DEEPSEEK_API_KEY = "Aqui iria la API key de Deepseek, darse de alta en https://platform.deepseek.com/"

# Creamos una funcion para llamar a la API de Deepseek

def llamar_api_deepseek(api_key):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "Escribe un poema breve sobre la vida"
            }
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()

# Llamamos a la API y guardamos la respuesta en una variable
respuesta_json = llamar_api_deepseek(DEEPSEEK_API_KEY)
print(json.dumps(respuesta_json, indent=4))
