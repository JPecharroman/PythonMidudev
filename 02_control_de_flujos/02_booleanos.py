from os import system
system("cls")

# Booleanos en Python

# Los booleanos son valores logicos que solo pueden tener dos valores: True o False

# Operadores de comparacion, que nos devolveran un booleano(True o False)

# Igualdad
# ==
print("1 = 1", 1 == 1) # Devuelve True
# !=
print("1 != 1", 1 != 1) # Devuelve False

# Mayor que
# >
print("1 > 1", 1 > 1) # Devuelve False
# >=
print("1 >= 1", 1 >= 1) # Devuelve True

# Menor que
# <
print("1 < 1", 1 < 1) # Devuelve False
# <=
print("1 <= 1", 1 <= 1) # Devuelve True

# En Python las comparaciones son lexicograficas, esto es, podemos comparar cadenas de texto por su valor lexicografico
print("\nComparacion de cadenas de texto")
print("¿Es b mayor que a?", "a" < "b") # Devuelve True, "a" tiene menor valor que "b"
print("¿Es A mayor que a?", "a" < "A") # Devuelve False, las minusculas tienen mayor valor que las mayusculas
print("¿Es ac mayor que ab?", "ab" < "ac") # Devuelve True, "ab" tiene menor valor que "ac" ya que "b" tiene menor valor que "c"
print("¿Es aa mayor que ab?", "ab" < "aa") # Devuelve False, "ab" tiene mayor valor que "aa" ya que "b" tiene mayor valor que "a"

print("¿Es hola menor o igual que HOLA?", "hola" <= "HOLA") # Devuelve False, las minusculas tienen menor valor que las mayusculas

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

print("\nTabla de verdad de condicionales booleanos")
print("AND")
print("True and True =", True and True) # Devuelve True
print("True and False =", True and False) # Devuelve False
print("False and True =", False and True) # Devuelve False
print("False and False =", False and False) # Devuelve False
print("OR")
print("True or True =", True or True) # Devuelve True
print("True or False =", True or False) # Devuelve True
print("False or True =", False or True) # Devuelve True
print("False or False =", False or False) # Devuelve False
print("NOT")
print("not True =", not True) # Devuelve False
print("not False =", not False) # Devuelve True

# Podemos evaluar variables no booleanas como booleanas, ya lo vimos en el archivo de casteos, transformacion de tipos
numero = 0
if numero: # Evalua la variable numero como booleana, si es 0, es False, si es distinto de 0, es True
    print("El numero es distinto de 0")
else:
    print("El numero es 0")

numero = 1
if numero: # Evalua la variable numero como booleana, si es 0, es False, si es distinto de 0, es True
    print("El numero es distinto de 0")
else:
    print("El numero es 0")

# En el caso de las cadenas de texto, si la cadena de texto es vacia, es False, si la cadena de texto es distinta de vacia, es True
nombre = ""
if nombre: # Evalua la variable nombre como booleana, si es la cadena vacia, es False, si es distinta de vacia, es True
    print(f"Hola! {nombre}")
else:
    print("El nombre introducido esta vacio")

nombre = "Jorge"
if nombre: # Evalua la variable nombre como booleana, si es la cadena vacia, es False, si es distinta de vacia, es True
    print(f"Hola! {nombre}")
else:
    print("El nombre introducido esta vacio")



