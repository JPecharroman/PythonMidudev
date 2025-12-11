# If en Python

# Antes de nada, vamos a importar el modulo os para poder usar la funcion system() que nos permite ejecutar comandos del sistema operativo
# import os
# Mas adelante veremos lo que son modulos, de momento lo que nos importa es que importamos el modulo os para poder usar la funcion system() y limpiar la terminal con "cls"
# os.system("cls")
# Podemos importar solo la funcion que nos interesa del modulo, en este caso, la funcion system(), esto es aconsejable en terminos de rendimiento, 
# ya que no importamos todo el modulo, sino solo la funcion que nos interesa y ahorramos memoria.
from os import system
system("cls")
# Usamos la funcion system() para limpiar la terminal, con "cls" o "clear", dependiendo del sistema operativo
# "clear" es para Linux y Mac
# "cls" es para Windows

# La sentencia if nos permite ejecutar un bloque de codigo si se cumple una condicion
"""
nombre, genero = input("Introduce tu nombre y tu genero(M: Masculino, F: Femenino): ").split(" ")
"""

# El condicional if nos permite ejecutar un bloque de codigo si se cumple una condicion, Python detecta la condicion y ejecuta el bloque de codigo si se cumple
# Python sabe lo que pertence al bloque de codigo asociado al if, gracias a la indentacion, es decir, los espacios en blanco que se ponen al inicio de cada linea
# Por lo tanto, todo lo que esté indentado pertenece al bloque de codigo asociado al if

"""
if genero == "M":
    print(f"Hola {nombre}, eres un hombre")
elif genero == "F": # elif es una abreviatura de else if, nos permite ejecutar este bloque de codigo si no se cumple la condicion del primer if
    print(f"Hola {nombre}, eres una mujer")
else: # else es una abreviatura de else, nos permite ejecutar este bloque de codigo si no se cumple la condicion de ninguno de los if anteriores
    print("Genero no valido")
"""

# elif y else son opcionales, nos sirven para mayor control del flujo de ejecucion del programa pero podemos hacer un if sin ellos.

# Vemos que al introducir "m" o "f" el programa nos da un error, recordar que Python es case sensitive, es decir, distingue entre mayusculas y minusculas
# debemos por tanto redefinir los flujos condicionales con la funcion upper()
# upper() es una funcion que convierte todos los caracteres de una cadena de texto a mayusculas, en nuestro caso, la variable genero
"""
if genero.upper() == "M":
    print(f"Hola {nombre}, eres un hombre")
elif genero.upper() == "F":
    print(f"Hola {nombre}, eres una mujer")
else:
    print("Genero no valido")
"""

# Por abreviar la ejecucion del programa iremos poniendo """ """ para comentar bloques de codigo, si queremos ejecutar el codigo descomentamos el bloque de codigo
# Podemos anidar varias sentencias if con elif
"""
vocal = input("Introduce una vocal: ")
if vocal.lower() == "a":
    print(f"{vocal} es una vocal")
elif vocal.lower() == "e":
    print(f"{vocal} es una vocal")
elif vocal.lower() == "i":
    print(f"{vocal} es una vocal")
elif vocal.lower() == "o":
    print(f"{vocal} es una vocal")
elif vocal.lower() == "u":
    print(f"{vocal} es una vocal")
else:
    print(f"{vocal} no es una vocal")
"""

# Anidamiento de condiciones para control de flujo de datos
# Podemos anidar varias sentencias if mediante el uso de operadores logicos AND, OR y NOT

"""
edad, nacionalidad = input("Introduce tu edad y tu nacionalidad: ").split(" ")
"""

"""
if int(edad) >= 18 and nacionalidad == "Española":
    print("Puedes votar en España")
elif int(edad) >= 18 and nacionalidad != "Española":
    print("Puedes votar, pero no en España")
elif int(edad) < 18 and int(edad) > 0:
    print("No puedes votar")
else:
    print("La edad, o la nacionalidad, introducida no son validas")
"""

# Mismo problema que vimos anteriormente con las mayusculas, si no introducimos exactamente el termino que buscamos, el programa nos da un error
# Por lo tanto, debemos redefinir los flujos condicionales con la funcion upper()
"""
if int(edad) >= 18 and nacionalidad.upper() == "Española".upper():
    print("Puedes votar en España")
elif int(edad) >= 18 and nacionalidad.upper() != "Española".upper():
    print("Puedes votar, pero no en España")
elif int(edad) < 18 and int(edad) > 0:
    print("No puedes votar")
else:
    print("La edad, o la nacionalidad, introducida no son validas")
"""

# Tabla de verdad de condicionales booleanos
# AND
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# OR
# True or True = True
# True or False = True
# False or True = True
# False or False = False
# NOT
# not True = False
# not False = True

# Ejemplo de flujo con el condicional if y el booleano OR
dia = "Sabado"
if dia.upper() == "SABADO" or dia.upper() == "DOMINGO":
    print("Es fin de semana")
else:
    print("No es fin de semana")

# Ejemplo de flujo con el condicional if y el booleano NOT
dia = "Lunes"
if not (dia.upper() == "SABADO" or dia.upper() == "DOMINGO"): 
# Evaluamos la condicion entre parentesis, nos devuelve false, ya que no es ni sabado ni domingo, le damos la vuelta con not devolviendonos true y entramos por el if
    print("No es fin de semana")
else:
    print("Es fin de semana")

# Podemos anidar condicionales if, PERO NO UNA BUENA PRACTICA Y DEBE EVITARSE
edad = 66
if edad >= 18:
    if edad <= 65:
        print("Puedes trabajar")
    else:
        print("Puedes trabajar, pero deberias jubilarte")
else:
    print("No puedes trabajar")

# En su lugar, debemos usar el condicional if, en este caso, con el booleano AND
if edad >= 18 and edad <= 65:
    print("Puedes trabajar")
elif edad > 65:
    print("Puedes trabajar, pero deberias jubilarte")
else:
    print("No puedes trabajar")

# Condicion ternaria
# [valor si se cumple la condicion] if [condicion] else [valor si no se cumple la condicion]
# Es una forma de simplificar el condicional if, es diferente a lo que estamos acostumbrados y puede ser confusa, por lo que no es muy recomendable usarla
edad = 18
print(f"Tienes {edad} años y puedes votar") if edad >= 18 else print(f"Tienes {edad} años y no puedes votar")
edad =   17
print(f"Tienes {edad} años y puedes votar") if edad >= 18 else print(f"Tienes {edad} años y no puedes votar")