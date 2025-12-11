# Variables en Python

# En Python no es necesario declarar el tipo de la variable, solo se le asigna el valor
# nombre_variable = valor

# Por convencion python usa snake_case para nombres de variables

cadena_texto = "Hola Mundo"
numero_entero = 1
numero_flotante = 1.1
numero_complejo = 1+1j
booleano = True
nulo = None

print(cadena_texto)
print(numero_entero)
print(numero_flotante)
print(numero_complejo)
print(booleano)
print(nulo)

# Podemos reasignar valores a variables
cadena_texto = 1 #Hemos cambiado el valor de la variable cadena_texto y su tipo de dato
numero_entero = "Hola Mundo" #Hemos cambiado el valor de la variable numero_entero y su tipo de dato
print(cadena_texto)
print(numero_entero)
print(type(cadena_texto))
print(type(numero_entero))
# El tipado de datos en Python es dinamico, es decir, el tipo de dato de una variable puede cambiar y se define por el valor que le asignemos

# Python es de tipado fuerte, es decir, no se puede asignar un valor de un tipo de dato a una variable de otro tipo de dato
# Lo vimos en el casteo de tipos de datos, print("10" + 10) da error

# Para usar este tipo de valores podemos castearlos, por ejemplo, print(int("10") + 10) o usar las cadenas formateadas, f-string, o format().
nombre = "Jorge"
edad = 30
print(f"{nombre} tiene {edad} años") # Podemos usar dos tipos de datos distintos, ya que edad es de tipo entero y lo usamos dentro de una cadena de texto
print("{} tiene {} años".format(nombre, edad)) # Podemos usar dos tipos de datos distintos, ya que edad es de tipo entero y lo usamos dentro de una cadena de texto


# Forma NO RECOMENDADA de dar valores a variables de modo mas rapido, se separan los valores con comas
nombre, edad, genero = "Jorge", 30, "Masculino"

# No es recomendable usar en python el modo de definir una variable de tipo camelCase
nombreCompleto = "Jorge" # aunque no rompemos el codigo, no es recomendable

# No existen constantes en python, por convencion se usan mayusculas para simular constantes, pero no deja de ser una variable y le podemos cambiar el valor
PI = 3.14159
PI = "Hola Mundo"
print(PI)

# Tipado de variables
# nombre_variable: tipo_de_dato = valor
numero_entero: int = 1 # Le decimos a python que en numero_entero se espera un valor de tipo entero y se le asigna el valor 1
# Peeeeeero, al ser de tipado dinamico, si le asignamos un valor de otro tipo de dato, python no nos da error
numero_entero = "Hola Mundo"
print(numero_entero)
print(type(numero_entero))
# El :tipo_de_dato es solo una forma de indicarle a python que tipo de dato esperamos que sea la variable, no obliga a python a nada


