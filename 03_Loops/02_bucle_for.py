# Bucle For en Python

# El bucle for en Python es un bucle de codigo que se ejecuta un numero finito de veces

# Sintaxis del bucle for
"""
for variable in iterable:
    codigo
else:
    codigo
"""

# Ejemplo de bucle for
from os import system
system("cls")   # Limpiamos la terminal

print("\nBucle for")
for i in range(1, 11):
    print(f"El numero actual es: {i}")

# Podemos usar break para salir del bucle for
print("\nBucle for con break")
for i in range(1, 11):
    print(f"El numero actual es: {i}")
    if i == 5:
        break

# Podemos usar continue para saltar la iteracion actual, no rompe el bucle, solo salta la iteracion actual
print("\nBucle for con continue")
for i in range(1, 11):
    i += 1
    if i == 5:
        continue
    print(f"El numero actual es: {i}")

# Podemos usar else para ejecutar codigo cuando la condicion del bucle for sea falsa
print("\nBucle for con else")
for i in range(1, 11):
    print(f"El numero actual es: {i}")
    i += 1
else:
    print("El bucle for ha terminado")

print("\n")
# La funcion enumerate() nos permite obtener el indice y el valor de cada iteracion
# enumerate() nos devuelve un objeto iterable que contiene el indice y el valor de cada iteracion
# debemos poner dos variables, la primera variable siempre es el indice y la segunda es el valor
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
for indice, dia in enumerate(lista): # indice y dia son las variables que capturan el indice y el valor, de la lista, en cada iteracion
    print(f"Dia de la semana {indice + 1}: {dia}")


# Podemos anidar bucles for, especialmente util para recorrer listas de listas, matrices.
print("\nBucle for anidado")
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista_interna in lista:
    for numero in lista_interna:
        print(numero, end=" ")
    print("\n")

# Bucle for en una linea, comprension de listas, en ingles list comprehension, vamos a poner los dias de la semana en Mayusculas.
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lista_comprension = [dia.upper() for dia in lista]
print(lista_comprension)

# Comprehesion de listas con condicion if
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lista_comprension = [dia.upper() for dia in lista if dia != "Viernes"]
print(lista_comprension)
# Ejemplo tipico de uso de comprension de listas con condicion if es devolver la lista de numeros que cumplen cierta condicion, por ejemplo son pares o impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(f"Los numeros pares en {numeros} son: {numeros_pares}")
numeros_impares = [numero for numero in numeros if numero % 2 != 0]
print(f"Los numeros impares en {numeros} son: {numeros_impares}")

# Comprehesion de listas con condicion if y else
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares_impares = ["par" if numero % 2 == 0 else "impar" for numero in numeros]
print(numeros_pares_impares)

