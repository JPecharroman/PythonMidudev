# Objetivo:
# Crear un programa que calcule cuantas veces aparece la letra 'R' y la letra 'J' en una cadena de texto
# Si el numero de 'R' es mayor que el de 'J', o el numero de 'J' es mayor que el de 'R', la funcion devolver False
# Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
# Si no hay ninguna 'R' ni 'J' la funcion debe devolver True, ya que se entiende que 'R' = 'J' = 0

# Creamos la funcion que recibe como parametro la cadena de texto y cuenta el numero de 'R' y 'J'
from os import system
system("cls")
# Funcion case sensitive
def contar_r_j(texto: str) -> bool:
    """
    Funcion que recibe como parametro la cadena de texto y cuenta el numero de 'R' y 'J'
    Si el numero de 'R' es mayor que el de 'J', o el numero de 'J' es mayor que el de 'R', la funcion devolver False
    Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
    Si no hay ninguna 'R' ni 'J' la funcion debe devolver True, ya que se entiende que 'R' = 'J' = 0

    :param texto: str
    :return: bool
    :raises ValueError: Si el parametro no es una cadena de texto
    """
    if not isinstance(texto, str):
        raise ValueError("El parametro debe ser una cadena de texto")
    
    contador_r = 0
    contador_j = 0
    for letra in texto:
        if letra == 'R': # Buscamos la letra 'R' en la cadena de texto, en principio seremos case sensitive
            contador_r += 1
        elif letra == 'J': # Buscamos la letra 'J' en la cadena de texto, en principio seremos case sensitive
            contador_j += 1
    print(f"El numero de veces que aparece en el tecto R es {contador_r}")
    print(f"El numero de veces que aparece en el tecto J es {contador_j}")
    if contador_r > contador_j or contador_j > contador_r: # Si el numero de 'R' es mayor que el de 'J', o el numero de 'J' es mayor que el de 'R', la funcion devolver False
        return False
    else: # Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
        return True

# Funcion case insensitive
def contar_r_j_insensitive(texto: str) -> bool:
    """
    Funcion que recibe como parametro la cadena de texto y cuenta el numero de 'R' y 'J'
    Si el numero de 'R' es mayor que el de 'J', o el numero de 'J' es mayor que el de 'R', la funcion devolver False
    Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
    Si no hay ninguna 'R' ni 'J' la funcion debe devolver True, ya que se entiende que 'R' = 'J' = 0

    :param texto: str
    :return: bool
    :raises ValueError: Si el parametro no es una cadena de texto
    """
    if not isinstance(texto, str):
        raise ValueError("El parametro debe ser una cadena de texto")
    
    contador_r = 0
    contador_j = 0
    texto_upper = texto.upper()
    # Contamos el numero de veces que aparece una letra con count()
    contador_r = texto_upper.count('R')
    print(f"El numero de veces que aparece en el tecto R o r es {contador_r}")
    contador_j = texto_upper.count('J')
    print(f"El numero de veces que aparece en el tecto J o j es {contador_j}")
    return True if contador_r == contador_j else False # Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
    # Podemos hacerlo todo en una sola linea
    # return True if texto_upper.count('R') == texto_upper.count('J') else False.

# Funcion minimalista

def contar_r_j_minimalista(texto: str) -> bool:
    """
    Funcion que recibe como parametro la cadena de texto y cuenta el numero de 'R' y 'J'
    Si el numero de 'R' es mayor que el de 'J', o el numero de 'J' es mayor que el de 'R', la funcion devolver False
    Si el numero de 'R' y 'J' es igual, la funcion debe devolver True
    Si no hay ninguna 'R' ni 'J' la funcion debe devolver True, ya que se entiende que 'R' = 'J' = 0

    :param texto: str
    :return: bool
    :raises ValueError: Si el parametro no es una cadena de texto
    """
    if not isinstance(texto, str):
        raise ValueError("El parametro debe ser una cadena de texto")

    # Simplificamos la funcion a una sola linea de codigo, pasamos texto a mayusculas y contamos el numero de veces que aparece 'R' y 'J'
    # y evaluamos si son iguales, retornando True o False si lo son o no.
    return texto.upper().count('R') == texto.upper().count('J')

texto = "Joder, que bueno estaba el jamon que comi con Ramon Ramirez, Jaja"
if(contar_r_j(texto)):
    print("El universo esta en equilibrio")
else:
    print("El universo no esta en equilibrio")

# Hagamos lo mismo con una funcion que sea case insensitive
if(contar_r_j_insensitive(texto)):
    print("El universo esta en equilibrio, si el universo es case insensitive")
else:
    print("El universo no esta en equilibrio, si el universo es case insensitive")

# Veamos si nos funciona la funcion minimalista
if(contar_r_j_minimalista(texto)):
    print("El universo esta en equilibrio, si el universo es minimalista y case insensitive")
else:
    print("El universo no esta en equilibrio, si el universo es minimalista y case insensitive")





    
    