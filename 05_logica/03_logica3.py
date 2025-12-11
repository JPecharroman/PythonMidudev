# Objetivo: 
# Dado un array de numeros y un numero objetivo, encuentra los dos primeros numeros del array que sumen el numero objetivo
# Retornar los indices de los dos numeros en el array
# Si no hay dos numeros que sumen el numero objetivo, retornar None

from os import system
system("cls")

# Buscamos una solucion minimalista, la mas simple posible, como en los dos casos anteriores.
# Veamos la logica del problema
# Tenemos un numero objetivo y debemos encontrar dos numeros en el array que sumen el numero objetivo
# Esto es, el primer numero que cogemos del array lo restamos al numero objetivo y buscamos si el resultado esta en el array
# Si esta, retornamos los indices de los dos numeros

# Pero hay otro elemento a tener en cuenta, que no debemos repetir indices, no podemos ir hacia atras, ya que esos ya estan checkeados
# si estamos en el indice 4, quiere decir que ya hemos comprobado los indices 0, 1, 2 y 3 y no hemos encontrado solucion
# por lo que no debemos volver a comprobar los indices 0, 1, 2 y 3.

# Si no esta, repetimos el proceso con el siguiente numero del array
# Si no hay dos numeros que sumen el numero objetivo, retornar None

# Definamos la funcion
def encuentra_indices(array:list[int], objetivo:int) -> tuple[int, int] | None:
    """
    Funcion que recibe como parametro una lista de numeros y un numero objetivo y devuelve los indices de los dos numeros que sumen el numero objetivo
    
    :param array: list[int]
    :param objetivo: int
    :return: tuple[int, int] | None
    :raises ValueError: Si el parametro no es una lista de numeros
    """
    if not isinstance(array, list):
        raise ValueError("El parametro debe ser una lista")
    
    # Le restamos el numero objetivo al primer numero del array
    # Si el resultado esta en el array, retornamos los indices de los dos numeros
    for indice, numero in enumerate(array):
        print(f"Iteracion numero {indice}")
        if objetivo-numero in array[indice + 1:]:
            # Ya sabemos que existe el numero buscado, por lo que retornamos los indices de los dos numeros
            # El primero lo tenemos en indice, el segundo lo hallaremos mediante el metodo index() de la lista
            # Como el metodo index() devuelve el indice del primer elemento que coincida con el valor buscado, debemos sumarle el indice + 1 para obtener el indice correcto
            return indice, array[indice + 1:].index(objetivo-numero) + (indice + 1)
    else: # Si no hay dos numeros que sumen el numero objetivo, retornar None
        return None

objetivo = 8
lista_numeros = [8, 3, 4, 6, 11, 4, 15, 6, 7]
print(encuentra_indices(lista_numeros, objetivo)) # Devuelve (0, 6)
