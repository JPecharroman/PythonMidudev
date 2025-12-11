# El scrapping, o raspado, es la tecnica de extraer informacion de una web, normalmente para analizarla.

# Ref: https://en.wikipedia.org/wiki/Web_scraping

"""
# Scrapping de Webs

# Primera opcion, con requests
# Ventajas: 
# - Es muy rapido y sencillo.
# Desventajas: 
# - No se salta paywalls y captchas.
# - No es muy robusto y no es muy seguro.
# - No puedes navegar por la web.
# - Muy manual, necesitas expresiones regulares para extraer la informacion.

# Segunda opcion, con BeautifulSoup
# Ventajas, es muy robusto y es muy seguro.
# Desventajas, es mas lento y mas complejo.

# Tercera opcion, con Selenium
# Ventajas, es muy robusto y es muy seguro.
# Desventajas, es mas lento y mas complejo.

"""

# Web Scapping en Python
# Vamos a hacer un ejemplo de web scrapping, para ello vamos a usar la libreria requests que instalamos con pip en el capitulo 08_requests.

from os import system
system('cls')
import requests, json

# Vamos a "robarle" contenido a Apple
url = 'https://www.apple.com/shop/buy-mac/macbook-air'

response = requests.get(url) # Hacemos una peticion GET a la url, normalmente GET es el metodo que usamos para pedir datos.
# Nos devuelve una respuesta que guardamos en la variable response.
# print(response.text) # Imprimimos la respuesta, sale en formato html.

if response.status_code == 200:
    print('Todo bien')
else:
    print('Algun error al hacer la peticion')


# Vamos a extraer la informacion de la web, usaremos expresiones regulares, Regex, para hallar informacion en el html.
# Vemos por la web, que el precion del macbook air es el que nos interesa, inspeccionamos el html y vemos que el precio esta en una etiqueta span con la clase price.
# <span class="rc-prices-fullprice" data-autom="full-price">$999.00</span>
# Usaremos la libreria re para hacer la busqueda.
import re
# Usaremos la funcion search de la libreria re para buscar la informacion.
patron = r'class="rc-prices-fullprice">(\$([0-9]+)\.[0-9]{1,2})' # El patron es la informacion que queremos buscar. 
# Tenemos la parte fija que va antes del precio a buscar, class="rc-prices-fullprice"> 
# y la parte variable, ya que el precio puede cambiar, que va despues del $. Representado por \$ ya que $ es un simbolo especial en regex.
# [0-9]+ significa que puede habra de 1 a n numeros.
# \. significa que debe haber un punto.
# [0-9]{1,2} significa que debe haber 1 o 2 numeros tras el punto.
busqueda = re.search(patron, response.text) # Buscamos la informacion en el html.
print(busqueda.group(1))

# Vamos a hallar el titulo de la web, que esta en una etiqueta h1 con la clase product-header-title.
patron_titulo = r'<title>(.*?)</title>'
# Patron a buscar, (.*?)
# . nos indica que empieza con cualquier caracter.
# * nos indica que puede haber 0 o n caracteres.
# ? nos indica que finaliza con cualquier caracter, 0 o 1 veces.
busqueda_titulo = re.search(patron_titulo, response.text)
print(f"El titulo de la web es: {busqueda_titulo.group(1)}")
