# Por claridad seguimos aqui con las expresiones regulares

import re
from os import system
system("cls")

# Metacaracteres
# Son caracteres que tienen un significado especial en las expresiones regulares, los usamos para formar patrones mas amplios

# . ^ $ * + ? { } [ ] ( ) | 
# . : Coincide con cualquier caracter
# ^ : Coincide con el inicio de una linea
# $ : Coincide con el final de una linea
# * : Coincide con cero o mas ocurrencias
# + : Coincide con una o mas ocurrencias
# ? : Coincide con cero o una ocurrencia
# { } : Coincide con un numero exacto de ocurrencias
# [ ] : Coincide con un rango de caracteres
# ( ) : Coincide con un grupo de caracteres
# | : Coincide con un alternativa de caracteres

Texto_ejemplo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Ejemplo 1
# El metacaracter . coincide con cualquier caracter
# Buscar todas las ocurrencias de la letra "p" en el texto seguida por cualquier caracter
patron = "p."
resultado = re.findall(patron, Texto_ejemplo)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)
# El metacaracter . es un unico caracter, no se cumplira si hay dos o mas caracteres
patron = "c.sa"
texto = "casa, caasa, causa, cosa, cisa, ciisa, cesa, ceesa"
resultado = re.findall(patron, texto)
print(f"El texto donde realizamos la busqueda es: {texto}")
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)
print("Vemos que nos nos encuentra la ocurrencia 'caasa', por ejemplo, porque el metacaracter . es un unico caracter, asi caasa no cumple con el patron")

# En Python, normalmente los patrones se designan anteponiendo el caracter r a la expresion del patron
patron = r"p."
# r nos ayudara con metacaracteres que lleven la barra invertida
# Por ejemplo, que pasa si en un texto quiero buscar cuantas veces hay un punto, no puedo poner el caracter de punto, ., porque es un metacaracter
# Entonces, para buscar un punto, usamos el caracter de escape, que es la barra invertida, \
patron = r"\." # Buscamos un punto
texto = "El coche es rojo. La casa es azul. El perro ladra. El gato maulla."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Con r tambien podemos usar metacaracteres que lleven la barra invertida
# \d coincide con un digito, cualquier numero del 0 al 9
patron = r"\d"
texto = "El coche es rojo. La 2 casa es azul. El 5 perro ladra. El gato maulla."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)
# Encontrar todos los numeros que esten juntos, usamos el metacaracter +
patron = r"\d+"
texto = "El coche es rojo. 123. El gato maulla. 456."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)
# Encontrar todos los numeros que esten juntos, un numero determinado de veces, usamos el metacaracter {n}
patron = r"\d{5}"
texto = "El coche es rojo. 123. El gato maulla. 45678. Paco anda67890. 2345."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Ejemplo 2
# Detectar si hay algun numero de telefono de españa en una lista de numeros pasados como texto
patron = r"\+34 6\d{2} \d{3} \d{3}"
texto = "+34 678 123 456, +33 722 122 234, +45 1234 12 12, +34 912 123 123, +34 665 234 221"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# \w, coincide con cualquier caracter alfanumerico, es decir, cualquier numero o letra, tanto a-z, como A-Z y 0-9 ó _
patron = r"\wl"
texto = "El coche es rojo. La 2 casa es azul. El 5 perro ladra. El gato maulla."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# \W, coincide con cualquier caracter no alfanumerico, salto de linea, espacio en blanco, tabulador, puntos, comas, etc
patron = r"\Wm" # Buscamos cualquier caracter no alfanumerico al que siga una m
texto = "El coche es rojo. La 2 casa es azul. El 5 perro ladra. El gato maulla."
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# \s, coincide con cualquier espacio en blanco, tabulador, salto de linea, etc
patron = r"\s\w" # Buscamos cualquier espacio en blanco, salto de linea, tabulador, etc al que siga una letra
texto = "El coche es rojo.\nLa 2 casa es azul.\tEl 5 perro ladra. El gato maulla." # \n salto de linea, \t tabulador
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Metacaracter ^, coincide con el inicio de una linea, normalmente se usa para verificar que una linea comienza con un patron
patron = r"^El" # Buscamos cualquier linea que comience con 'El'
texto = "El coche es rojo"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {patron}, en el texto")
else:
    print(f"No encontrado el patron buscado, {patron}, en el texto")
texto2 = "La casa es azul"
resultado2 = re.search(patron, texto2)
if resultado2:
    print(f"Encontrado el patron buscado, {patron}, en el texto")
else:
    print(f"No encontrado el patron buscado, {patron}, en el texto")

# Metacaracter $, coincide con el final de una linea, normalmente se usa para verificar que una linea termina con un patron
patron = r"rojo$" # Buscamos cualquier linea que termine con 'rojo'
texto = "El coche es rojo"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {patron}, en el texto")
else:
    print(f"No encontrado el patron buscado, {patron}, en el texto")
texto2 = "La casa es azul"
resultado2 = re.search(patron, texto2)
if resultado2:
    print(f"Encontrado el patron buscado, {patron}, en el texto")
else:
    print(f"No encontrado el patron buscado, {patron}, en el texto")

# Ejemplo 3
# Buscar los ficheros con extension .py en una lista de ficheros pasados como texto
patron = r"\w+\.py" # Buscamos cualquier fichero que tenga al menos un caracter antes del punto y que termine con .py
texto = "fichero.txt, .py, fichero, fichero.exe, fichero.py, fichero2.py, fichero3.py, mifichero.jav, tufichero.css, fichero.html, fichero4.py"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Metacaracter \b, coincide con el inicio o fin de una palabra
# con \b podemos buscar palabras completas
patron = r"\bperro\b" # Buscamos la palabra 'perro' completa
texto ="perro perrote perroja perroto perrot perro"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Metacaracter |, coincide con el OR
# con | podemos buscar varias opciones {}
# Buscamos cualquier fichero que tenga al menos un caracter antes del punto y que termine con .css o .html
patron = r"\w+\.css|\w+\.html"
texto = "fichero.txt, .py, fichero, fichero.exe, fichero.py, fichero2.py, fichero3.py, mifichero.jav, tufichero.css, fichero.html, fichero4.py"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)


# Cuantificadores
# Son metacaracteres que se colocan al final del patron para indicar cuantas veces se repite el patron
# +, coincide con el patron una o mas veces
# ?, coincide con el patron cero o una vez
# *, coincide con el patron cero o mas veces
# {n}, coincide con el patron exactamente n veces
# {n,}, coincide con el patron n o mas veces
# {n,m}, coincide con el patron entre n y m veces

# Interrogacion ?: cero o una vez
patron = r"\w?b" # cualquier caracter alfanumerico 0 o 1 vez seguido de una b
texto = "cabra, abra, bra, aver, beras"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Exactamente n veces {n}
patron = r"\w{3}" # cualquier caracter alfanumerico, que aparezcan seguidos, exactamente 3 veces
texto = "cabra, abra, bra, aver, beras"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# De n a m veces {n,m}
patron = r"\w{4,6}" # cualquier caracter alfanumerico, que aparezcan seguidos, entre 4 y 6 veces
texto = "cabra, abra, bra, aver, beras"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Ejemplo 4
# Encuentra las palabras en un texto dado que tengan entre 4 y 6 caracteres
patron = r"\w{4,6}" # cualquier caracter alfanumerico, que aparezcan seguidos, entre 4 y 6 veces. 
#Pero buscamos palabras exactas, asi que el patron debera estar entre \b
patron = r"\b\w{4,6}\b"
texto = "lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Sets
# Son metacaracteres que se colocan entre corchetes [] para indicar un conjunto de caracteres
patron = r"[aeiou]" # Buscamos cualquier vocal
texto = "lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
resultado = re.findall(patron, texto)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Ejemplo 5
# Detecta si el texto pasado es un correo electronico
patron = r"\w+@\w+\.\w+" # Buscamos cualquier texto que tenga al menos un caracter antes del @, seguido de al menos un caracter, seguido de un punto, seguido de al menos un caracter
texto = "micorreo@midudev.com"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {texto} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Pero este patron no es el mas optimo para detectar correos electronicos, por ejemplo este correo electronico no se detectaria: mi_correo@midudev.com
# porque _ no es un alfanumerico contenido en \w
# Refinemos el patron con un set
patron = r"[\w_]+@\w+\.\w+"
texto = "mi_correo@midudev.com"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {texto} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Hagamos los mismo para acotar lo que despues de la arriba, cualquier alfanumerico o guion o punto
# Tambien refinamos mas el set incial, añadiendo el punto, el %, el + y el -
patron = r"[\w._%+-]+@[\w.-]+\.[\w]+" # Aqui tenemos dos sets, uno para el usuario y otro para el dominio. Nos faltaria refinar lo que hay tras el punto final
texto = "mi_cor.reo@midu-dev.com"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {texto} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Este correo seria legal si no refinamos lo que hay tras el punto final
texto = "mi_cor.reo@midu-dev.comcomcom"
resultado = re.search(patron, texto)
if resultado:
    print(f"Encontrado el patron buscado, {texto} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Tras el punto final solo debe admitir alfanumericos en un rango de 2 a 4 caracteres
patron = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}" # Refinamos lo que hay tras el punto final, solo alfanumericos en un rango de 2 a 4 caracteres
texto = "mi_cor.reo@midu-dev.comom"
resultado = re.search(patron, texto)
system("cls")
print(f"Buscamos el correo electronico: {texto}")
if resultado:
    print(f"Encontrado el patron buscado, {resultado.group()} es un correo electronico")
    print("Pero esto no es verdaderamente correcto, el problema es que no acotamos que se cumpla de principio a fin y coge la parte que cumpla el patron, corta la m final de comom")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Acotamos el patron con ^ y $ para que solo se cumpla si se cumple de principio a fin
patron = r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}$" # Acotamos el patron con ^ y $ para que solo se cumpla si se cumple de principio a fin
# ^ indica que el patron debe comenzar con lo que le sigue
# $ indica que el patron debe terminar con lo que le antecede
# [a-zA-Z]{2,4} indica que debe haber entre 2 y 4 caracteres alfabeticos, mayusculas o minusculas. No pueden ser numeros

texto = "mi_cor.reo@midu-dev.comom"
resultado = re.search(patron, texto)
system("cls")
print(f"Buscamos el correo electronico: {texto}")
if resultado:
    print(f"Encontrado el patron buscado, {resultado.group()} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico") # no encontro el patron, no hay nada en resultado.group()

texto = "mi_cor.reo@midu-dev.com"
resultado = re.search(patron, texto)
print()
print(f"Buscamos el correo electronico: {texto}")
if resultado:
    print(f"Encontrado el patron buscado, {resultado.group()} es un correo electronico")
else:
    print(f"No encontrado el patron buscado, {texto} no es un correo electronico")

# Uso tipico de sets es encontrar palabras similares que difieran en uno o dos caracteres.
lista = "man ñam pan fan ban van tan"
print(f"Encuenta las palabras que empiezen por m, f o b en la lista {lista}")
patron = r"[mfb][a-zA-Z]{2}" # Buscamos cualquier palabra que empiece con m, f o b y despues tenga exactamente 2 caracteres mas
resultado = re.findall(patron, lista)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)
# [mfb] indica que el patron debe comenzar con m, f o b, esto es un set.

# Negar las busquedas con ^
patron = r"\b[^mfb]an\b" # Buscamos cualquier palabra que no empiece con m, f o b y despues tenga exactamente 2 caracteres mas
resultado = re.findall(patron, lista)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)

# Busquedas que empiecen por cualquier cosa que no sea un numero
patron = r"\D[\w]{2,}" # Buscamos cualquier caracter que no sea un numero
resultado = re.findall(patron, lista)
print(f"He encontrado {len(resultado)} ocurrencias del patron buscado, {patron}, en el texto")
print(resultado)