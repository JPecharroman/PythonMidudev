# Uso de Try except con bucle while en Python

# El try except nos permite capturar los errores que puedan ocurrir en el bucle while
# En este ejemplo, el bucle while se ejecutara hasta que el usuario introduzca un numero del 0 al 9
# Si el usuario introduce un dato que no es un numero, el bucle while se rompera y dara error
# Para evitar esto, usamos try except, que nos permite capturar el error y ejecutar el codigo que queramos
lista_de_numeros = [0,1,2,3,4,5,6,7,8,9]
numero = 10
while numero not in lista_de_numeros:
    try: # Capturamos el valor introducido por el usuario mediante un try except
        numero = int(input("Introduce un numero del 0 al 9: "))
    except ValueError: # Capturamos el error que puede ocurrir si el usuario introduce un dato que no es un numero
        print("El valor introducido no es numerico, introduce un numero valido")
    except Exception as e: # Capturamos cualquier otro error que pueda ocurrir
        print(f"Ha ocurrido un error: {e}")
    finally: # Se ejecuta siempre, haya ocurrido un error o no
        print("Me ejecuto siempre porque soy un finally")
else: # Si el valor introducido es un numero, salimos del bucle while y ejecutamos el codigo que queramos
    print(f"El numero {numero} esta en la lista")

# Tipos de errores que podemos capturar, algunos de los mas usuales son:
# Exception: Error general, cuando ocurre un error que no se puede capturar
# ValueError: Error de valor, cuando el valor introducido no es el esperado
# TypeError: Error de tipo, cuando el tipo de dato introducido no es el esperado
# ZeroDivisionError: Error de division por cero, cuando se divide por cero
# FileNotFoundError: Error de archivo no encontrado, cuando el archivo no existe
# IndexError: Error de indice, cuando el indice introducido no es el esperado
# KeyError: Error de clave, cuando la clave introducida no es la esperada
# NameError: Error de nombre, cuando el nombre introducido no es el esperado
# SyntaxError: Error de sintaxis, cuando la sintaxis del codigo no es correcta
# TabError: Error de tabulacion, cuando la tabulacion del codigo no es correcta
# IndentationError: Error de indentacion, cuando la indentacion del codigo no es correcta
# ImportError: Error de importacion, cuando el modulo o paquete no se puede importar
# ModuleNotFoundError: Error de modulo no encontrado, cuando el modulo o paquete no se puede importar
# AttributeError: Error de atributo, cuando el atributo no existe
# KeyboardInterrupt: Error de interrupcion, cuando el usuario interrumpe el programa
# RecursionError: Error de recursion, cuando se produce una recursion infinita

