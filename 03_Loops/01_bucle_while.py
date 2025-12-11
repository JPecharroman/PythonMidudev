# Bucles While en Python

# El bucle while en Python es un bucle de codigo que se ejecuta mientras una condicion sea verdadera

# Sintaxis del bucle while
"""

while condicion:
    codigo
else:
    codigo

"""

# Ejemplo de bucle while
from os import system
system("cls")   # Limpiamos la terminal

print("\nBucle while")
numero = 1
while numero <= 10:
    print(f"El numero actual es: {numero}")
    numero += 1 # Incrementamos el numero en 1 en cada iteracion, evitar bucles infinitos

# Podemos usar break para salir del bucle while
print("\nBucle while con break")
numero = 1
while numero <= 10:
    print(f"El numero actual es: {numero}")
    if numero == 5:
        break
    numero += 1

# Podemos usar continue para saltar la iteracion actual, no rompe el bucle, solo salta la iteracion actual
print("\nBucle while con continue")
numero = 1
while numero <= 10:
    numero += 1
    if numero == 5:
        continue
    print(f"El numero actual es: {numero}")

# Podemos usar else para ejecutar codigo cuando la condicion del bucle while sea falsa
print("\nBucle while con else")
numero = 1
while numero <= 10:
    print(f"El numero actual es: {numero}")
    numero += 1
else:
    print("El bucle while ha terminado")

# else es util cuando usamos break en el bucle while, nos indica que se han efectuado todas las iteraciones que esperabamos, cosa que no pasaria si salta un break

# Uso del bucle while para pedir informacion por pantalla al usuario, verificamos que los datos introducidos cumplen los parametros que esperamos
print("\nUso del bucle while para pedir informacion por pantalla al usuario")
lista_de_numeros = [0,1,2,3,4,5,6,7,8,9]
numero = 10
while numero not in lista_de_numeros:
    numero = int(input("Introduce un numero del 0 al 9: ")) 
    # Pedimos al usuario que introduzca un numero, este sera de tipo string por defecto, por lo que lo casteamos a entero
else:
    print(f"El numero {numero} esta en la lista")

# Existe un problema evidente con este ejeplo anterior, al castear el dato introducido por el usuario, si el usuario introduce un dato que no sea un numero, 
# el bucle while se rompera y dara error, para evitar esto, usamos try except, lo veremos en el siguiente archivo, 01_while_con_try.py.


