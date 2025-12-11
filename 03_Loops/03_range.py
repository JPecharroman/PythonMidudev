# range() en Python

# range() es una funcion que nos permite generar una secuencia de numeros

# Por defecto, range() comienza en 0 y termina en el numero que le indiquemos menos 1
# Por ejemplo, range(1, 11) comienza en 1 y termina en 10
# no es necesario que range() tenga los dos valores, podemos pasarle solo un valor, range(11) comienza en 0 y termina en 10
# range() es iterable, por lo que podemos usarlo con el bucle for o while
# range() admite un tercer valor que es el paso, por defecto es 1, pero podemos indicarle un valor mayor o menor
# Por ejemplo, range(1, 11, 2) comienza en 1 y termina en 10, pero solo imprimira los numeros pares
# el paso en range() puede usar valores negativos, por ejemplo, range(10, 0, -1) comenzaria en 10 y terminaria en 1
# range() no es una lista, esto es, no esta en memoria, se genera en el momento de la iteracion y desaparece al finalizarla
# por lo que no es recomendable usar range() con listas grandes, ya que se generaria en memoria y consumiria muchos recursos
for indice in range(11):
    print(f"El numero actual es: {indice}")

# Con el bucle for podemos iterar sobre una lista, tupla, diccionario, etc... sobre cualquier cosa que sea iterable
texto = "Esta cadena de texto es iterable"
for letra in texto:
    print(f"{letra}", end="/")

# Comprension de listas con range()
numeros_pares_impares = ["par" if numero % 2 == 0 else "impar" for numero in range(1, 11)]
print(numeros_pares_impares)

# Aun mas simple es hallar los pares, o impares, con range() si le añadimos un salto
pares = [numero for numero in range(0, 10, 2)]
print(pares)
impares = [numero for numero in range(1, 10, 2)]
print(impares)

# Ejercicio tipico con range(), y for, es imprimir la tabla de multiplicar
for primer_numero in range(1, 10):
    print(f"Tabla del {primer_numero}")
    for segundo_numero in range(1, 10):
        print(f"{primer_numero} x {segundo_numero} = {primer_numero * segundo_numero}")
    print("\n")