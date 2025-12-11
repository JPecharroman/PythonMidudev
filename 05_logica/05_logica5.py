# Objetivo: 
# Tenemos dos listas de numeros, ambas con la misma longitud.
# Cada numero de la lista 1 se enfrenta al numero, en su misma posicion, de la lista 2.

# Si el valor de la lista 1 es mayor que el de la lista 2, obtenemos la diferencia entre ellos y se lo sumamos al siguiente valor de la lista 1.
# Si el valor de la lista 2 es mayor que el de la lista 1, obtenemos la diferencia entre ellos y se lo sumamos al siguiente valor de la lista 2.
# Si son iguales, no se suma nada.

# Como resultado final debemos obtener un string que nos devuelva:
# Si el ganador final es un numero de la lista 1, retornaremos el ultimo valor ganador, restar valor[lista1] - valor[lista2] y retornar el string "Ganador lista 1: valor"
# Si el ganador final es un numero de la lista 2, retornaremos el ultimo valor ganador, restar valor[lista2] - valor[lista1] y retornar el string "Ganador lista 2: valor"
# Si no hay ganador, retornar el string "Empate"

# Definamos la/s funcion/es

# SOLUCION 1 - Minimalista
# Empezemos por la solucion minimalista, la mas simple posible, como en los dos casos anteriores.
# Tenemos dos funciones de enteros, ambas con la misma longitud, esto es, el mismo numero de elementos.
# La solucion a este caso es sencilla, sumamos los valores de ambas listas y hallamos su diferencia, el valor mas alto es el ganador.

def enfrentamiento_listas(lista1:list[int], lista2:list[int]) -> str:
    """
    Funcion que recibe como parametro dos listas de numeros y devuelve el string "Ganador lista 1: valor" si el valor mas alto es de la lista 1, "Ganador lista 2: valor" si el valor mas alto es de la lista 2 y "Empate" si no hay ganador
    
    :param lista1: list[int]
    :param lista2: list[int]
    :return: str
    :raises ValueError: Si el parametro no es una lista de numeros
    """
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise ValueError("El parametro debe ser una lista")
  
    # Si la suma de lista1 es mayor que la suma de lista2, retornamos el string "Ganador lista 1: valor", siendo valor la diferencia entre las sumas
    if sum(lista1) > sum(lista2):
        return f"Ganador lista 1: {sum(lista1)-sum(lista2)}"
    # Si la suma de lista2 es mayor que la suma de lista1, retornamos el string "Ganador lista 2: valor", siendo valor la diferencia entre las sumas
    elif sum(lista1) < sum(lista2):
        return f"Ganador lista 2: {sum(lista2)-sum(lista1)}"
    # Si la diferencia es 0, retornamos el string "Empate"
    else:
        return "Empate"


lista1 = [2,4,2] # Siguiendo el principio de solucion minimalista, la suma de esta lista es 8
lista2= [3,3,4] # Siguiendo el principio de solucion minimalista, la suma de esta lista es 10
# Por tanto la solucion que debe devolvernos nuestra funcion es "Ganador lista 2: 2".

# Veamoslos
print(enfrentamiento_listas(lista1, lista2)) # Devuelve "Ganador lista 2: 2"

# Veamos un ejemplo con ganador lista 1, para ellos la suma de lista1 debe ser mayor que la suma de lista2
lista1 = [2,4,2] # Suma 8
lista2 = [1,2,3] # Suma 6
print(enfrentamiento_listas(lista1, lista2)) # Devuelve "Ganador lista 1: 2"

# Veamos un ejemplo con empate, para ellos la suma de lista1 debe ser igual que la suma de lista2
lista1 = [2,4,2] # Suma 8
lista2 = [1,2,5] # Suma 8
print(enfrentamiento_listas(lista1, lista2)) # Devuelve "Empate"

# Como vemos, la solucion minimalista es correcta y tremendamente eficiente, ya que no necesitamos de bucles para hallar la solucion.
# Aunque con esta solucion quiza nos estemos saltando el enunciado, que nos pedia enfrentar los numeros de ambas listas


# SOLUCION 2 - Respetando, a medias, el enunciado
# Vamos a enfrentar los numeros de ambas listas, pero lo haremos en una sola iteracion
# El principio de la solucion es sencilla, si el numero de lista1 es mayor que el de lista2, le sumamos la diferencia al siguiente numero de lista1
# PERO, si es menor, lo que hacemos es restarle la diferencia al siguiente numero de lista1, esto es, es indiferente en 4-6, sumarle 2 al siguente elemento de la lista2
# que restarle 2 al siguiente elemento de la lista1.
# Veamos un ejemplo
#   lista1 = [2,4,2]
#   lista2 = [4,2,3]
#   El primero valor de lista2 es mayor que el de lista1, obteniendo la diferencia vemos que es 2.
#   siguiendo el enunciado deberiamos sumarle 2 al siguiente valor de lista2, es decir, sumarle 2 al valor 2 de lista2.
#   las nuevas listas nos quedarian: lista1 = [2,4,2] y lista2 = [4,4,3]
#   con lo que la siguiente iteracion deberiamos comparar 4 por lista1 y 4 por lista2, empate.
#   Con la solucion que hemos aportado, solo vamos modificando lista1, lista2 permanece igual, asi que lo que hacemos es sumar la diferencia, en este caso restamos
#   ya que la diferencia de primer valor de lista1 - primer valor de lista2 es negativa, 2-4 = -2, es decir, restamos 2 al siguiente valor de lista1, es decir, 4-2 = 2.
#   ahora comparamos los siguientes valores de lista1 y lista2, 2 y 2, empate. Nuestra solucion es analoga a la anterior.

def enfrentamiento_listas2(lista1:list[int], lista2:list[int]) -> str:
    """
    Funcion que recibe como parametro dos listas de numeros y devuelve el string "Ganador lista 1: valor" si el valor mas alto es de la lista 1, "Ganador lista 2: valor" si el valor mas alto es de la lista 2 y "Empate" si no hay ganador
    
    :param lista1: list[int]
    :param lista2: list[int]
    :return: str
    :raises ValueError: Si el parametro no es una lista de numeros
    """
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise ValueError("El parametro debe ser una lista")
    
    for indice, numero in enumerate(lista1):
        if indice == len(lista1) - 1: # Si es el ultimo numero de lista1, no tenemos un indice+1, comparamos solo los ultimos.
            lista1[indice] = numero - lista2[indice]
        else:
            lista1[indice+1] = lista1[indice+1] + (numero - lista2[indice]) # Sumamos la diferencia entre el numero de lista1 y el de lista2 al siguiente numero de lista1  
    # Salimos del bucle, miramos el valor del ultimo numero de lista1, si es positivo, lista1 es el ganador, si es negativo, lista2 es el ganador, si es 0, empate
    if lista1[-1] > 0: # Entramos en lista1 por su ultima posicion
        return (f"Ganador lista 1: {lista1[-1]}")
    elif lista1[-1] < 0:
        # Convertimos en positivo la diferencia para mostrarla, valor absoluto con la funcion abs().
        return (f"Ganador lista 2: {abs(lista1[-1])}")
    else:
        return ("Empate") 
    
    


lista1 = [2,4,2]
lista2 = [4,2,3]
# Basandonos en la solucion1, vemos que deberia devolvernos "Ganador lista 2: 1"
print(enfrentamiento_listas(lista1, lista2))
# Hallamos la solucion2
print(enfrentamiento_listas2(lista1, lista2))


# SOLUCION 3 - Respetando el enunciado
# Cumplamos el enunciado, hagamos las modificaciones en ambas listas.

def enfrentamiento_listas3(lista1:list[int], lista2:list[int]) -> str:
    """
    Funcion que recibe como parametro dos listas de numeros y devuelve el string "Ganador lista 1: valor" si el valor mas alto es de la lista 1, "Ganador lista 2: valor" si el valor mas alto es de la lista 2 y "Empate" si no hay ganador
    
    :param lista1: list[int]
    :param lista2: list[int]
    :return: str
    :raises ValueError: Si el parametro no es una lista de numeros
    """ 
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise ValueError("El parametro debe ser una lista")
    
    for indice, numero in enumerate(lista1):
        # Primera cosa que debemos tener en cuenta, no salirnos de rango, por lo que debemos comprobar que el indice+1 no sea mayor que la longitud de la lista
        if indice == len(lista1) - 1: # Si es el ultimo numero de lista1, no tenemos un indice+1, comparamos solo los ultimos.
            if lista1[indice] > lista2[indice]:
                return (f"Ganador lista 1: {lista1[indice]-lista2[indice]}")
            elif lista1[indice] < lista2[indice]:
                return (f"Ganador lista 2: {lista2[indice]-lista1[indice]}")
            else:
                return ("Empate")
            break # Rompemos el bucle, no nos interesa continuar ya que es el ultimo elemento de la lista, no hay indice+1

        # Comparamos el numero de lista1 con el de lista2, si es mayor, sumamos la diferencia al siguiente numero de lista1
        if numero > lista2[indice]:
            lista1[indice+1] = lista1[indice+1] + (numero - lista2[indice])
        # Si es menor, sumamos la diferencia de lista2[indice] - numero al siguiente numero de lista2
        elif numero < lista2[indice]:
            lista2[indice+1] = lista2[indice+1] + (lista2[indice] - numero)
        # Si es igual, no hacemos nada
        else:
            pass

lista1 = [2,4,2] # suma 8
lista2 = [4,2,3] # suma 9
print(enfrentamiento_listas3(lista1, lista2))