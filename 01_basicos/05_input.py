# Input en Python

# la funcion input() nos permite obtener un valor introducido por el usuario

# La primera opcion es usar la funcion input() asociada a una variable
print("Hola, ¿Cual es tu nombre?")
nombre = input()
print(f"Hola, tu nombre es {nombre}")

# La segunda opcion es usar la funcion input() con el texto con el que queremos pedirle los datos al usuario directamente en la funcion input()
numero = input("Introduce un numero: ")
print(numero)
print(type(numero))
print(f"El valor introducido por teclado es {numero} y es de tipo {type(numero)}")
# Como vemos, el valor introducido por el usuario es de tipo cadena de texto, por lo que si queremos usarlo como numero, o cualquier otro tipo de dato, debemos castearlo
numero = int(numero)
print(f"Casteamos el valor introducido por teclado para pasarlo a tipo entero: Ahora {numero} es de tipo {type(numero)}")

# Para obtener varios valores a la vez, podemos usar la funcion input() con el separador de valores que queramos
nombre, apellido = input("Introduce tu nombre y apellido: ").split(" ") # la funcion split() divide la cadena de texto en una lista de cadenas de texto.
# El separador de valores sera un espacio en blanco, parametro que se le pasa a la funcion split(), si no ponemos separador, por defecto sera un espacio en blanco
# Lo primero que introduzca el usuario sera el valor de nombre, y lo segundo sera el valor de apellido
print(f"Hola, tu nombre es {nombre} y tu apellido es {apellido}")

# Igual que existe la funcion split() para separar cadenas de texto, mediante un separador de valores pasado como parametro, 
# existe la funcion join(), que une una lista de cadenas de texto en una cadena de texto, mediante un separador de valores, que es el encargado de llamar a la funcion join()
nombre_completo = "-".join([nombre, apellido])
print(nombre_completo)

