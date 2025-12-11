# Funciones en Python

# Una funcion es un bloque de codigo que se ejecuta cuando se le llama
# Son reutilizables y parametrizables. Sirven paara tareas especificas.

# La palabra reservada def nos permite crear una funcion

"""

def nombre_de_la_funcion(parametro1, parametro2, ...):
    #docstring
    #codigo
    #return, si retorna algo ira dentro de este return

"""

from os import system
system("cls")
def primera_funcion():
    print("Hola mundo")

def segunda_funcion(nombre):
    print(f"Hola mundo, yo soy {nombre}")

primera_funcion() # Esta primera funcion es reutilizable
segunda_funcion("Jorge") # Esta segunda funcion es reutilizable y parametrizable
segunda_funcion("Pepe")

# Funciones con retorno
def suma(a:int, b:int) -> int: # con los int le aportamos informacion al usuario de esta funcion, le indicamos que espera dos enteros como parametros y retorna un entero
    return a + b

print("La suma de 1 + 2 es: ", suma(1, 2))

# Es importante documentar nuestras funciones, para ello usamos el docstring, asi como indicamos que tipo de datos espera y retorna
# Usamos el doble comilla triple para documentar nuestras funciones
# con :param indicamos que tipo de dato espera la funcion  
# con :return indicamos que tipo de dato retorna la funcion
# con :type indicamos que tipo de dato espera la funcion
# con :rtype indicamos que tipo de dato retorna la funcion
# con :raise indicamos que tipo de error puede lanzar la funcion
# con :raises indicamos que tipo de error puede lanzar la funcion
# con :except indicamos que tipo de error puede capturar la funcion
# con :var indicamos que tipo de dato es una variable
# con :ivar indicamos que tipo de dato es una variable de instancia
# con :cvar indicamos que tipo de dato es una variable de clase
def suma(a:int, b:int) -> int:
    """
    Esta funcion espera dos enteros como parametros y retorna un entero
    :param a: int
    :param b: int
    :return: int
    """
    return a + b

print(f"La suma de 3 + 4 es: {suma(3, 4)}")
print(suma.__doc__) # el metodo __doc__ nos permite ver el docstring de la funcion

# Valores por defecto en los parametros
def division(a:int, b:int = 1) -> float:
    """
    Esta funcion espera dos enteros como parametros y retorna un flotante
    :param a: int
    :param b: int
    :return: float
    :raises ZeroDivisionError: Si el segundo parametro es cero

    """
    return a / b

numero1 = 10
numero2 = 0
try:
    print(f"La division de {numero1} / {numero2} es: {division(numero1, numero2)}")
    # b seria opcional, si no lo pasamos usaria el valor por defecto, que es 1
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    print(f"La division de {numero1} / valor por defecto de numero2 es: {division(numero1)}")
except ZeroDivisionError as e:
    print(f"Error: {e}")


# Argumentos por clave en funciones
def describir_persona(nombre:str, edad:int, genero:str) -> str:
    """
    Esta funcion espera tres parametros y retorna un string
    :param nombre: str
    :param edad: int
    :param genero: str
    :return: str
    """
    return f"{nombre} tiene {edad} años y es de genero {genero}"

print(describir_persona("Jorge", 30, "Masculino"))
#Si cambiaramos el orden de introduccion de los parametros, la funcion funcionaria correctamente, esto es, el programa no se romperia, pero no tendria sentido
print(describir_persona("Jorge", "Masculino", 30))
# Mi edad no puede ser "Masculino" y mi genero no puede ser 30
# Esto lo arreglamos pasando los parametros por clave
print(describir_persona(nombre="Jorge", genero="Masculino", edad=30))
# Vemos que aunque en la definicion de la funcion el parametro edad esta en segunda posicion, se lo podemos pasar como parametro por clave con independencia de su orden

# Funciones con parametros variables, argumentos de longitud variable (*args)
def suma(*args) -> int:
    """
    Esta funcion espera un numero indeterminado de enteros como parametros y retorna un entero
    :param args: int
    :return: int
    """
    suma = 0
    for arg in args:
        suma += arg
    return suma
    # Podriamos usar la funcion sum() para hacer lo mismo
    # return sum(args)

print(suma(1, 2, 3, 4, 5))
print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Funciones con parametros variables, argumentos de longitud variable (*args) y keyword arguments (**kwargs)
# Argumentos de longitud variable (*args) son argumentos que pueden recibir un numero indeterminado de parametros
# Keyword arguments (**kwargs) son argumentos que se pasan con clave-valor, un numero indeterminado de veces

# Ejemplo de funcion con argumentos de clave valor variables (**kwargs)
def mostrar_info(**kwargs) -> str:
    """
    Esta funcion espera un numero indeterminado de enteros como parametros y retorna un entero
    :param kwargs: int
    :return: int
    """
    for key, value in kwargs.items(): # items() nos devuelve una lista de tuplas con las claves y valores, en ese orden
        print(f"{key}: {value}", end=" ")
    print() # Salto de linea

# Numero de parametros variables y clave-valor variables
mostrar_info(nombre="Jorge", edad=30, genero="Masculino")
mostrar_info(nombre="Pepe", edad=25, genero="Masculino", ciudad="Madrid")
mostrar_info(nombre="Paco", genero="Masculino", edad=25, casado=True, sub=False)

