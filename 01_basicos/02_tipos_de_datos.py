# Tipos de datos en Python

# Tipos de datos primitivos
# Enteros (int)
print(1)
# Para saber el tipo de dato de una variable usamos la funcion type
print(type(1))
# El mayor numero que se puede representar en Python es 2^63-1
print(2**63-1) #9223372036854775807
# El menor numero que se puede representar en Python es -2^63
print(-2**63) #-9223372036854775808


# Flotantes (float)
print(1.1)
# Para saber el tipo de dato de una variable usamos la funcion type
print(type(1.1))
# Los numeros con notacion cientifica se representan con e y son de tipo float
print(1.1e10)
print(type(1.1e10))

# Complejos (complex), parte real e imaginaria
print(1+1j)
print(type(1+1j))


# Booleanos (bool)
print(True)
print(type(True))
print(False)

# Cadenas de texto(str)
print("Hola")
# Para saber el tipo de dato de una variable usamos la funcion type
print(type("Hola"))
# Con tres comillas podemos imprimir cadenas de texto en varias lineas
print("""
    Imprimimos
    varias
    lineas
""")

# Nulos (None), representa la ausencia de valor
print(None)
print(type(None))
