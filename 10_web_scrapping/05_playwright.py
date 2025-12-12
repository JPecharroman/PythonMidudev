# Web Scrapping con Playwright en Python

# Ref: https://playwright.dev/
# Ref: https://playwright.dev/python/docs/intro
# Ref: https://playwright.dev/python/docs/test-runners

# Playwright es una biblioteca para automatizar el navegador, es decir, para controlar el navegador desde Python.
# Playwright levanta un navegador para que puedas interactuar con la web, como si fueras un usuario real.
# Playwright es mas lento, y costoso, que BeautifulSoup y Selenium, pero es mas robusto y seguro.
# Es mas facil saltarte paywalls y captchas.
# Es mas facil navegar por la web.
# 

# Instalacion
""" pip3 install pytest playwright """

# Despues debemos instalar los navegadores
""" playwright install """

# Despues debemos instalar el modulo de pytest para correr los tests
""" pip3 install playwright pytest-playwright """

# Para hacer los tests, desde la terminal usamos pytest
""" pytest archivo.py -v 

    -v es para ver mas detalles
    
"""

# Cargamos el ejemplo que viene en la pagina de referencia de Playwright https://playwright.dev/python/docs/intro
# test_example.py

import re # Importamos la libreria re para hacer la busqueda c  on regex.
from playwright.sync_api import Page, expect # Importamos la libreria playwright para automatizar el navegador.
from os import system # Importamos la libreria os para limpiar la terminal.
system('cls')

def test_has_title(page: Page): # Definimos la funcion test_has_title, comprobamos si la pagina del test tiene titulo.
    page.goto("https://playwright.dev/") # Navegamos a la pagina, vamos a la url.

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright")) # Comprobamos si la pagina tiene el titulo correcto, debe contener la palabra Playwright.

def test_get_started_link(page: Page): # Definimos la funcion test_get_started_link, comprobamos si la pagina del test tiene enlace.
    page.goto("https://playwright.dev/") # Navegamos a la pagina, vamos a la url.

    # Click the get started link.
    page.get_by_role("link", name="Get started").click() # Hacemos click en el enlace con nombre Get started.

    # Despues de hacer click en el enlace, vamos a comprobar si la pagina tiene el encabezado, con algun h1, h2, h3, h4, h5, h6, Installation visible.
    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible() # Comprobamos si la pagina tiene el encabezado Installation visible.


