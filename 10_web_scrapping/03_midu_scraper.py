# Wikipedia no tiene meta de open graph
# Usamos la web de midudev para hacer el scraper y probar si obtenemos los metas de open graph.

from os import system
system('cls')

from requests import get
from bs4 import BeautifulSoup

url = 'https://midu.dev'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# Buscamos los metas de open graph
og_titulo = soup.find('meta', {'property': 'og:title'}) # Buscamos la etiqueta meta con el atributo property y el valor og:title.
print(f"El titulo de la pagina web es: {og_titulo.get('content')}\n") 
# obtenemos en og_titulo el contenido de la etiqueta meta con el atributo property y el valor og:title. Dentro de este valor buscamos la etiqueta content para imprimir
# su contenido.

og_descripcion = soup.find('meta', {'property': 'og:description'}) # Buscamos la etiqueta meta con el atributo property y el valor og:description.
print(f"La descripcion de la pagina web es: {og_descripcion.get('content')}\n")
# obtenemos en og_descripcion el contenido de la etiqueta meta con el atributo property y el valor og:description. Dentro de este valor buscamos la etiqueta content 
# para imprimir su contenido.

og_imagen = soup.find('meta', {'property': 'og:image'})
print(f"La imagen de la pagina web es: {og_imagen.get('content')}\n")
# obtenemos en og_imagen el contenido de la etiqueta meta con el atributo property y el valor og:image. Dentro de este valor buscamos la etiqueta content 
# para imprimir su contenido.

# Otra forma de pasar parametros a buscar, no usar un diccionario sino directamente la clave y el valor.
"""
og_imagen = soup.find('meta', property='og:image') # Buscamos la etiqueta meta con el atributo property y el valor og:image.
print(f"La imagen de la pagina web es: {og_imagen.get('content')}\n")
"""
