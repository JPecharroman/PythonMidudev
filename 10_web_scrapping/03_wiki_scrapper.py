# Vamos a hacer scrapping de la pagina web de wikipedia

# Siemore que haces una peticion estas enviando tu user agent.
# User agent es un identificador que te dice que navegador y sistema operativo estas usando.
# Algunas paginas web no te permiten hacer scrapping si no envias tu user agent.
# Para enviar tu user agent puedes usar el parametro headers en la peticion.
# Gracias a ello podemos "tunear" la peticion para que se comporte como si viniera de un navegador.

# Ref: https://realpython.com/beautiful-soup-web-scraper-python/ 
# Ref: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup
from os import system
system('cls')

url = 'https://es.wikipedia.org/wiki/Web_scraping'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Al conectarme a la pagina web, le envio mi user agent.
# De esta manera la pagina web sabe que estoy usando un navegador y no un scraper.
# Hay algunos user agents que son mas comunes que otros.
# Por ejemplo, el de chrome es el mas comun.
# Puedes buscar en google "user agent" para ver los mas comunes.
# En este caso, el user agent que he puesto es el de chrome.
# Otro user agent que las web no suelen querer bloquear es el de googlebot.
# Googlebot es el user agent de google.
# Puedes buscar en google "googlebot user agent" para ver el user agent de google.
# Googlebot es un crawler que google usa para indexar las paginas web.
# Ref: https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers?hl=es
# En esta web puedes acceder a los robots de google para rastrear las paginas web.

"""
headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36'
}
"""

# El bot de google puede abrir puertas en webs problematicas, en principio wikipedia nos permitira acceder con un user agent propio.
# Sin embargo, si el user agent es demasiado personalizado, puede ser bloqueado.
# Por lo tanto, es recomendable usar un user agent comun, como el de chrome. El que pusimos arriba.

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# Extraemos los titulos de la web, etiqueta h1
titulos = [titulo.text for titulo in soup.find_all('h1')]
print(f"El titulo/s de la pagina web es: {titulos}")
# Subtitulo/s de la web, etiqueta h2
subtitulos = [subtitulo.text for subtitulo in soup.find_all('h2')]
print(f"El subtitulo/s de la pagina web es: {subtitulos}")

# Enlaces de la web, etiqueta a
# enlaces = [enlace.get('href') for enlace in soup.find_all('a')] # Obtenemos el atributo href de la etiqueta a, esto es, recuperamos la url.
# Esto me devuelve enlaces relativos, no son direcciones absolutas y por tanto no podre navegar por la web, necesito las url absolutas.
# Por lo tanto, debo unir la url base con el enlace relativo.

# Importamos desde urllib.parse la funcion urljoin
# urljoin une dos urls, una base y una relativa.
from urllib.parse import urljoin
enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]
print(f"Los enlaces de la pagina web son: {enlaces}\n")

