# Vamos a hacer un pequeño programa para analizar el seo de una web en Python.
# Vamos a hacerlo con la libreria requests y BeautifulSoup.

import requests
import argparse
# argparse nos permite crear argumentos para el programa. Es un "parseador" de argumentos. Esto es, permite que el usuario pueda pasar argumentos al programa.
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from os import system
system('cls')

# Creamos una funcion para hacer la peticion GET
def scrape_url(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Error al hacer la peticion GET a la url: {url}')
    else: 
        print(f'La peticion fue exitosa, Status code: {response.status_code}')
        return response

# Creamos el parser de argumentos
parser = argparse.ArgumentParser(description='Analizador de SEO desde una URL pasada como argumento')
parser.add_argument('url', type=str, help='URL de la web donde queremos analizar el SEO')
args = parser.parse_args()
url = args.url

response = scrape_url(url)
# Creamos un objeto BeautifulSoup para parsear el HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extraemos el titulo de la web, como titulo solo hay, deberia, podemos acceder a el directamente
# titulo = soup.find('title').get_text()
titulo = soup.title.string
# print(f'El titulo de la web es: {titulo}') - Imprimiremos la descripcion de la web mas adelante usando escape codes

# Extraemos la descripcion de la web
descripcion = soup.find('meta', {'name': 'description'}).get('content')
# print(f'La descripcion de la web es: {descripcion}') - Imprimiremos la descripcion de la web mas adelante usando escape codes

# ANSII escape codes, añadir colores a la salida de datos por consola y los datos se ordenen por colores
# Ref: https://en.wikipedia.org/wiki/ANSI_escape_code

# Para empezar un escape code usamos \033[
# \033[31m es el color rojo
# \033[32m es el color verde
# \033[33m es el color amarillo
# \033[34m es el color azul
# \033[35m es el color morado
# \033[36m es el color celeste
# \033[37m es el color blanco
# \033[0m es el color por defecto
# Toda la gama de colores la podemos obtener en la tabla ANSI
# AL finalizar el escape code usamos \033[0m para volver al color por defecto
print(f"\033[31mEl titulo de la web es: {titulo}\033[0m")
# Cambiamos el background a azul y el foreground a blanco con ;
print(f"\033[47;34mLa descripcion de la web es: {descripcion}\033[0m") #BG;FG BG47 es blanco y FG34 es azul

# Extraemos los h1 de la web
titulos_h1 = [titulo.get_text() for titulo in soup.find_all('h1')]
# Imprimimos los titulos usando escape codes y un FG Verde
for titulo in titulos_h1:
    print(f"\033[32m{titulo}\033[0m")


