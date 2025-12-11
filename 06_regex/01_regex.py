# Expresiones Regulares en Python

# Que son las expresiones regulares?
# Son una secuencia de caracteres que forman un patron de busqueda

# Por que usan expresiones regulares?
# Son muy utiles para validar datos, por ejemplo, para validar un email. Tambien nos sirven para buscar, y reemplazar cadenas de texto.

# Patrones comunes
# email
# telefono
# fecha
# hora
# ip
# url
# codigo postal
# negrita en texto, **texto**
# cursiva en texto, _texto_
# texto tachado, ~texto~
# texto subrayado, __texto__

# ¿Por qué aprender RegEx?
# Busqueda avanzada de cadenas de texto, encontrar patrones en textos grandes de forma rapida
# Validacion de datos, asegurar que los datos introducidos son correctos
# Extraccion de datos, extraer informacion de un texto
# Sustitucion de datos, reemplazar ciertos patrones

# Como usar expresiones regulares?
# Usando el modulo re

import re
from os import system
system("cls")

# Definamos un patron, una cadena de texto que vamos a buscar en otro texto
patron = "hola"
texto = "hola mundo"

# Metodo de busqueda del modulo re, search busca en todo el texto
resultado = re.search(patron, texto)
print(resultado) # El resultado es un objeto

# Al ser resultado un objeto, podemos acceder a sus atributos y metodos
print(resultado.start()) # Indica el indice donde comienza el patron
print(resultado.end()) # Indica el indice donde termina el patron
print(resultado.span()) # Indica el indice donde comienza y termina el patron
print(resultado.string) # Indica el texto en el que se hizo la busqueda
print(resultado.group()) # Indica el patron que se encontro

# Ejemplo 1
# Encuentra la primera ocurrencia del patron "IA" en el texto dado
# El texto sera "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las RegEx, para ir con cuidado"

patron = "IA"
texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las RegEx, para ir con cuidado"

resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {patron}, en el texto. Su posicion de inicio es {resultado.start()} y su posicion de fin es {resultado.end()}")
else:
    print(f"No se encontro el patron buscado, {patron}, en el texto")

# Encontrar un patron tantas veces como se repita en un texto, metodo findall
patron = "IA"
texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar la IA con las RegEx, para ir con cuidado"

resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
# Al ser resultado una lista, podemos acceder a sus atributos y metodos
# findall devuelve una lista con todas las ocurrencias del patron buscado, pero no nos devuelve la posicion de cada ocurrencia

# Metodo finditer
# Este metodo devuelve un iterador con todas las ocurrencias del patron buscado
resultado = re.finditer(patron, texto)
for i in resultado:
    print(f"Encontrado el patron buscado, {patron}, en el texto. Su posicion de inicio es {i.start()} y su posicion de fin es {i.end()}")

# Ejemplo 2
# Encuentra la cantidad de veces que aparece el patron "midu" en el texto dado e indica su posicion de inicio y fin
# El texto sera "Este es el curso de Python de Midudev. !Suscribete a midudev si te gusta este contenido!, midudev"

patron = "midu"
texto = "Este es el curso de Python de Midudev. !Suscribete a midudev si te gusta este contenido!, midudev"

resultado = re.finditer(patron, texto)
lista = list(resultado) # Transformamos el iterador en una lista
print(f"He encontrado {len(lista)} ocurrencias del patron buscado, {patron}, en el texto") 
# Al ser resultado un iterador, lo convertimos a lista para poder contar las ocurrencias
for indice in lista:
    print(f"Encontrado el patron buscado, {patron}, en el texto. Su posicion de inicio es {indice.start()} y su posicion de fin es {indice.end()}")

# Modificadores
# Modificadores son caracteres que se colocan al inicio del patron para modificar su comportamiento
# Modificadores
# re.IGNORECASE : Coincide con mayusculas y minusculas
# re.MULTILINE : Coincide con saltos de linea
# re.DOTALL : Coincide con caracteres especiales

patron = "IA"
texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la ia la puede cagar con las RegEx, para ir con cuidado. Ia peligrosa" 

resultado = re.finditer(patron, texto, re.IGNORECASE)
print()
print("Busqueda con ignorecase, no distingue entre mayusculas y minusculas")
for i in resultado:
    print(f"Encontrado el patron buscado, {i.group()}, en el texto. Su posicion de inicio es {i.start()} y su posicion de fin es {i.end()}")

# Reemplazar textos con re.sub()
patron = "IA"
substituye = "Manolo"
texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la ia la puede cagar con las RegEx, para ir con cuidado. Ia peligrosa" 

resultado = re.sub(patron, substituye, texto, flags=re.IGNORECASE) # flags=re.IGNORECASE para que no distinga entre mayusculas y minusculas
print()
print(f"Reemplazo de texto con re.sub(), reemplazando {patron} por {substituye}")
print(resultado)
