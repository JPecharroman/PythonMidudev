# Objetivo: Crear una funcion que reciba una lista de numeros y devuelva la suma de los numeros pares, solo los pares.

# Definamos la funcion
from os import system
system("cls")

# Como en el ultimo caso anterior buscamos una funcion minimalista, la mas simple posible. Pasamos por la funcion sumando solo los pares
# Tenemos la funcion sum() que suma todos los elementos de una lista
# Pero no queremos sumar todos los elementos, solo los pares
# Por lo que usamos una funcion lambda (numero for numero in lista if numero % 2 == 0) para generar una lista, temporal, solo con los pares
# Y luego sumamos todos los pares con la funcion sum()
def suma_pares(lista:list[int]) -> int:
    """
    Funcion que recibe como parametro una lista de numeros y devuelve la suma de los numeros pares
    
    :param lista: list[int]
    :return: int
    :raises ValueError: Si el parametro no es una lista de numeros
    """
    if not isinstance(lista, list): # Validamos que el parametro sea una lista con la funcion isinstance()
        raise ValueError("El parametro debe ser una lista") # raise se usa para lanzar una excepcion
    return sum(numero for numero in lista if numero % 2 == 0)

# Una funcion lambda es una funcion anonima que se puede usar en una sola linea de codigo
# En este caso la funcion lambda es (numero for numero in lista if numero % 2 == 0)
# El objetivo de uso de una funcion lambda es simplificar el codigo
# En este caso la funcion lambda genera una lista temporal, solo con los pares
# La funcion lambda se puede usar en cualquier lugar donde se pueda usar una funcion, se genera en el momento de su uso y se destruye una vez finalizada su ejecucion
    
suma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"La suma de la lista es {suma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
