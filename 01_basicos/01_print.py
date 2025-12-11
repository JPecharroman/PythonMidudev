# Por conveccion python usa snake_case para nombres de archivos, de ahi el nombre 01_print.py

# print es una funcion que muestra en la consola
# nuestro primer "programa" imprimir "Hola Mundo"
print("Hola Mundo")

# Podemos hacer cadenas de texto con comillas simples o dobles
print('Hola Mundo')
print("Hola Mundo")

# Podemos usar la comilla simple dentro de una cadena de comillas dobles
print("Hola 'Mundo'")

# Podemos usar la comilla doble dentro de una cadena de comillas simples
print('Hola "Mundo"')

# Podemos pasarle varios parametros de entrada a la funcion print
print("Hola", "Mundo", "desde", "Python") 
# El separador por defecto es el espacio en blanco, al imprimir esto vemos que nos imprime cada parametro separado por un espacio en blanco
# Si queremos cambiar el separador por defecto podemos usar el parametro sep
print("Hola", "Mundo", "desde", "Python", sep="-")

# Por defecto la funcion print termina con un salto de linea, si queremos cambiar esto podemos usar el parametro end
print("Hola", "Mundo", "desde", "Python", end=" ") # Cambiamos el salto de linea por un espacio en blanco con end
print("Esto se sigue imprimiendo en la misma linea")


