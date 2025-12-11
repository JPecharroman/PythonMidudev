# Web scrapping con BeautifulSoup en Python

# Ref: https://crummy.com/software/BeautifulSoup
# Version actual: 4.12.3
# Ref: https://crummy.com/software/BeautifulSoup/bs4/doc/
# La instalamos con pip, pip install bs4

# Vamos a hacer un ejemplo de web scrapping con BeautifulSoup, para ello vamos a usar la libreria requests que instalamos con pip en el capitulo 08_requests.
# bs4 no hace peticiones HTTP, por eso usamos requests.
import requests, json
# Importamos del paquete bs4 la clase BeautifulSoup.
from bs4 import BeautifulSoup

from os import system
system('cls')

# Url a scrapear
url ="https://www.apple.com/es/shop/buy-mac/macbook-air"

# Hacemos la peticion GET a la url.
response = requests.get(url)
if response.status_code == 200:
    print('Todo bien')
    sopa = BeautifulSoup(response.text, 'html.parser') # 'html.parser' es el parser que usamos para parsear el html.
    # print(sopa.prettify()) # Imprimimos la sopa, es decir, el html parseado.
else:
    print('Algo ha salido mal')

# Metodos que nos facilitan la vida con BeautifulSoup
# title, nos devuelve el titulo de la web.
titulo = sopa.title
if titulo:print(f"El titulo de la web es: {titulo.string}") # El metodo .string nos devuelve el contenido de la etiqueta. eliminado los tags html. (<title>Titulo</title> -> Titulo)

# Busquedas a partir de una etiqueta. tenemos en titulo la etiqueta title, ahora buscamos a partir del padre de title.
metadatos = titulo.parent.find_all('meta')
print(f"El numero de metadatos de esta web es: {len(metadatos)}")
indice = 0
for meta in metadatos:
    indice += 1
    print(f"{indice} - El nombre del meta es: {meta.get('name')} y el contenido es: {meta.get('content')}")

# Encontrar un elemento por su nombre. Buscamos el precio del macbook air.
precio = sopa.find('span', class_ = 'rc-prices-fullprice')
print(f"El precio del macbook air es: {precio.string}")
# Buscar todos los precios de la web y el nombre del producto asociado a el.
# Usamos find_all para buscar todos los productos.
# Una vez que tengamos los productos, sacamos su nombre y su precio.
productos = sopa.find_all(class_ = 'rc-productselection-item')
for producto in productos:
    nombre = producto.find(class_ = 'list-title').string
    precio = producto.find(class_ = 'rc-prices-fullprice').string
    print(f"El nombre del producto es: {nombre} y el precio es: {precio}")

# precios = sopa.find_all('span', class_ = 'rc-prices-fullprice')
# nombre = sopa.find_all(class_ = 'rc-productselection-item')
# print(f"El numero de precios de esta web es: {len(precios)}")
# print(f"El numero de nombres de esta web es: {len(nombre)}")
