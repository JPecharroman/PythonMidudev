# Diccionarios en Python

# Definamos el diccionario
# Un diccionario es una coleccion de datos indexada, desordenada y mutable
# Se define con llaves {} y tiene un par clave-valor.
# Ambos, clave y valor, pueden ser de cualquier tipo de datos, si son strings se definen entre comillas.

persona = { # Definicion del diccionario
    "nombre": "Jorge", # clave: valor, donde la clave es "nombre" y el valor es "Jorge"
    "apellido": "Herrero", # clave: valor, donde la clave es "apellido" y el valor es "Herrero"
    "edad": 30, # clave: valor, donde la clave es "edad" y el valor es 30
    1: "uno", # clave: valor, clave es de tipo int y valor es "uno"
    True: False # clave: valor, clave es de tipo bool y valor es False
}

from os import system
system("cls")

print(persona)
print(type(persona))

# Acceder a un valor, accedemos por la clave como si fuera un array
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])

# Podemos tener estructuras de datos anidadas
persona2 = {
    "nombre": "Jorge",
    "apellido": "Herrero",
    "edad": 30,
    "domicilio": { # Diccionario dentro de otro diccionario
        "calle": "Calle 1",
        "ciudad": "Ciudad 1",
        "pais": "Pais 1"
    },
    "hobbies": [ "Jugar", "Leer", "Correr" ] # Lista dentro de otro diccionario

}

# Para acceder a un valor anidado, accedemos por sus claves, como si fuera un array
print(persona2["domicilio"]["calle"])
print(persona2["hobbies"][0])

# De igual manera podemos cambiar valores dentro del diccionario
persona2["nombre"] = "Juan"
print(persona2)
persona2["domicilio"]["calle"] = "Calle 2"
print(persona2)
persona2["hobbies"][0] = "Ladrar"
print(persona2)

# Podemos agregar nuevas claves
persona2["profesion"] = "Programador"
print(persona2)

# Podemos eliminar claves con el metodo pop()
persona2.pop("edad")
print(persona2)

# Podemos eliminar claves con la funcion del
del persona2["apellido"]
print(persona2)

# La principal diferencia entre el metodo pop() y la funcion del es que pop() devuelve el valor de la clave eliminada
nombre = persona2.pop("nombre")
print(persona2)
print(nombre)

# Podemos eliminar todas las claves con el metodo clear()
persona2.clear()
print(persona2)

# Podemos eliminar el diccionario con la funcion del
persona2 = {"nombre": "Jorge", "apellido": "Herrero", "edad": 30}
print(persona2)
del persona2
# print(persona2) # Esto generaria un error ya que el diccionario ya no existe

# Otro metodo interesante es el metodo update(), que nos permite actualizar el diccionario, tambien puede recibir otro diccionario como parametro
persona3 = {"nombre": "Jorge", "apellido": "Herrero", "edad": 30}
persona3.update({"nombre": "Juan", "apellido": "Herrero", "edad": 30}) # Actualiza el diccionario persona3 cambiando el valor de la clave "nombre"
persona4 = {"nombre": "Jorge", "domicilio": "Calle 1", "casado": False}
persona4.update(persona3) # Actualiza el diccionario persona4, agregando las claves del diccionario persona3 y modificando los valores de las claves existentes
print(persona4) # {'nombre': 'Juan', 'domicilio': 'Calle 1', 'casado': False, 'nombre': 'Juan', 'apellido': 'Herrero', 'edad': 30}

# Con la palabra reservada in podemos verificar si una clave existe en el diccionario
print("nombre" in persona4) # True
print("apellidos" in persona4) # False, es apellido
print("edad" in persona4) # True
print("calle" in persona4) # False, es domicilio
print("casado" in persona4) # True

# Si queremos obtener todas las claves de un diccionario, podemos usar el metodo keys()
print(persona4.keys()) # dict_keys(['nombre', 'domicilio', 'casado', 'nombre', 'apellido', 'edad'])
print(type(persona4.keys())) # <class 'dict_keys'>
# Si queremos obtener todos los valores de un diccionario, podemos usar el metodo values()
print(persona4.values()) # dict_values(['Juan', 'Calle 1', False, 'Juan', 'Herrero', 30])
print(type(persona4.values())) # <class 'dict_values'>
# Si queremos obtener todas las claves y valores de un diccionario, podemos usar el metodo items(), lo devulve como una lista de tuplas clave-valor
print(persona4.items()) # dict_items([('nombre', 'Juan'), ('domicilio', 'Calle 1'), ('casado', False), ('nombre', 'Juan'), ('apellido', 'Herrero'), ('edad', 30)])
print(type(persona4.items())) # <class 'dict_items'>

# Vamos a solucionar el problema del ejercicio expuesto en el archivo 03_logica3.py con diccionarios
# Objetivo: 
# Dado un array de numeros y un numero objetivo, encuentra los dos primeros numeros del array que sumen el numero objetivo
# Retornar los indices de los dos numeros en el array
# Si no hay dos numeros que sumen el numero objetivo, retornar None

# Debemos hacerlo con un diccionario, usaremos el numero como clave y el indice como valor para crear un diccionario de numeros que ya hemos recorrido
# Cada nueva iteracion, comparamos el numero objetivo con el numero actual, si el numero objetivo menos el numero actual existe en el diccionario, 
# retornamos el indice del numero actual y el indice del numero objetivo

system("cls")
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
    
    # Creamos un diccionario para almacenar los numeros que hemos recorrido
    numeros = {}
    
    # Recorremos la lista de numeros
    for indice, numero in enumerate(array):
        # Si el numero objetivo menos el numero actual existe en el diccionario, retornamos el indice del numero actual y el indice del numero objetivo
        if objetivo-numero in numeros:
            return numeros[objetivo-numero], indice # Recordar que en el diccionario numeros guardamos el indice como valor, por eso pasamos el valor.
        # Si no existe, agregamos el numero actual al diccionario
        numeros[numero] = indice
        print(numeros) # Vamos listando los numeros que hemos recorrido
    else: # Si no hay dos numeros que sumen el numero objetivo, retornar None
        return None

numeros = [8, 3, 4, 6, 11, 4, 15, 6, 7]
objetivo = 8
print(encuentra_indices(numeros, objetivo))
# Esta solucion no es la optima, ni nos devuelve los indices de los dos primeros numeros que sumen el numero objetivo, serian (0, 6) y nos devuelve (2, 3)
# ni tampoco es la mas eficiente, ya que, ya que realiza muchas iteraciones innecesarias, la forma creada en el ejercicio 3_logica3.py es la mas eficiente.