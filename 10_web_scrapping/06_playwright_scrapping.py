# Vamos a hacer un ejemplo de web scrapping con Playwright en Python

import re
from playwright.sync_api import Page, expect, sync_playwright
from os import system
system('cls')

# Url a scrapear
url = "https://midudev.com/"

# Inicializamos el navegador
with sync_playwright() as p: # Usamos el metodo sync_playwright() para inicializar el navegador.
    browser = p.chromium.launch(headless=False) # chromium es el navegador que vamos a usar, basado en el navegador Chrome.
    page = browser.new_page() # Usamos el metodo new_page() para crear una nueva pagina, pestaña, en el navegador.
    page.goto(url) # Usamos el metodo goto() para ir a la url que pasamos como parametro.

    primer_articulo = page.locator("article a").first # Usamos el metodo locator() para obtener el primer articulo. Dentro de article, buscamos el primer enlace a.

    # Clickamos en el enlace.
    primer_articulo.click() # Usamos el metodo click() para hacer click en el enlace.

    page.wait_for_load_state("") # Esperamos a que la pagina se cargue completamente.

    primera_imagen = page.locator("main img").first # Usamos el metodo locator() para obtener la primera imagen dentro de main.
    src_imagen = primera_imagen.get_attribute("src") # Usamos el metodo get_attribute() para obtener el atributo src de la imagen.
    print(f"La primera imagen es: {src_imagen}")

    browser.close() # Cerramos el navegador.
    

    
    
