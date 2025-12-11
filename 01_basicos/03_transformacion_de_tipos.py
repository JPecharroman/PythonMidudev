# Transformacion de tipos en Python

# casteo a entero, int()
flotante = 1.1
entero = int(flotante)
print("EL numero flotante " + str(flotante) + " se convierte en el numero entero " + str(entero)) # Cuidado con las perdidas de precision
print("Aqui vemos el tipo de la variable entero ", type(entero))
# Un casteo especial es el casteo con round(), que redondea el numero
entero = round(flotante)
print("EL numero flotante " + str(flotante) + " se redondea como el numero entero " + str(entero))
print("Aqui vemos el tipo de la variable entero ", type(entero))
# Que pasa si redondeamos el .5?
entero = round(1.5)
print("EL numero flotante " + str(1.5) + " se redondea como el numero entero " + str(entero))
print("Aqui vemos el tipo de la variable entero ", type(entero))
entero = round(2.5)
print("EL numero flotante " + str(2.5) + " se redondea como el numero entero " + str(entero))
print("Aqui vemos el tipo de la variable entero ", type(entero))
# Es decir, tanto 1.5 como 2.5 se redondean al numero entero 2, esto es debido a que Python redondea los .5 al numero entero par mas cercano
# en el caso de 1.5 su entero par mas cercano es 2, y en el caso de 2.5 su entero par mas cercano es 2, ya que 4 esta mas lejos que 2.
# La explicacion de por que redondea los .5 al numero entero par mas cercano es por estadistica, si siempre redondeas hacia arriba, o hacia abajo
# rompemos la distribucion normal, es decir, la distribucion de los numeros redondeados 


print("\n")
# casteo a flotante, float()
entero = 1
flotante = float(entero)
print("EL numero entero " + str(entero) + " se convierte en el numero flotante " + str(flotante))
print("Aqui vemos el tipo de la variable flotante ", type(flotante))

print("\n")
# casteo a complejo, complex()
entero = 1
complejo = complex(entero)
print("EL numero entero " + str(entero) + " se convierte en el numero complejo " + str(complejo))
print("Aqui vemos el tipo de la variable complejo ", type(complejo))


print("\n")
# casteo a booleano, bool()
entero = 1
booleano = bool(entero)
print("EL numero entero " + str(entero) + " se convierte en el booleano " + str(booleano))
print("Aqui vemos el tipo de la variable booleano ", type(booleano))
# Los dos valores que se pueden convertir en False al castear a booleano son 0 y None, el resto, incluyendo negativos, se convierte en True
print("El valor None se convierte en el booleano ", bool(None))
print("El valor 0 se convierte en el booleano ", bool(0))
print("El valor -1 se convierte en el booleano ", bool(-1))
print("El valor 1 se convierte en el booleano ", bool(1))
# Casteando booleanos con cadenas de texto, el unico valor que se puede convertir en False es la cadena de texto vacia, el resto se convierte en True, 
# incluso la cadena de texto "False" se convierte en True
# Esto es porque Python distingue entre cadenas de texto con contenido y cadenas de texto vacias, las que tienen algo se consideran True
# y las que no tienen nada se consideran False
print(bool(""))
print(bool("Hola"))
print(bool("False"))

print("\n")
# casteo a cadena de texto, str()
entero = 1
cadena = str(entero)
print("EL numero entero " + str(entero) + " se convierte en la cadena de texto " + str(cadena))
print("Aqui vemos el tipo de la variable cadena ", type(cadena))


# Operaciones con tipos de datos distintos
print("La suma del entero 1 y de la cadena de texto '1', casteada a entero, es ", end="")
print(1+ int("1"))
print("Aqui vemos que el tipo de la operacion es entero: ", type(int("1") + 1))

print("\n")
print("La concatenacion de la cadena de texto '1' y el entero 1, casteado a cadena de texto, es ", end="")
print("1" + str(1))
print("Aqui vemos que el tipo de la operacion es cadena de texto: ", type("1" + str(1)))
