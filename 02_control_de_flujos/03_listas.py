from os import system
system("cls")

# Listas en Python

# Las listas son colecciones de datos ordenadas, mutables y pueden contener datos de diferentes tipos
lista_de_ejemplo = [1, "Hola", True, 3.14159] # Vemos que puede contener datos de diferentes tipos
# LAs listas en Python se puede definir poniendo los datos entre corchetes [] o con la funcion list()
lista_de_ejemplo = list([1, "Hola", True, 3.14159]) # list() lleva, tambien, los parametros entre corchetes []

lista_vacia = []
lista_vacia = list()

print("Listas en Python\n")
print("lista_de_ejemplo creada con corchetes = [1, \"Hola\", True, 3.14159]")
print("lista_de_ejemplo creada con list() = list([1, \"Hola\", True, 3.14159])")
print("lista_vacia creada con corchetes = []")
print("lista_vacia creada con list() = list()")
print("\n")

# Lista de listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
print("\n")
# Podemos representar una matriz con una lista de listas
print("Representacion de una matriz con una lista de listas")
for fila in lista_de_listas: # En caada iteracion recoge un valor de lista_de_listas, es decir, una fila, [1, 2, 3] en la primera iteracion, por ejemplo
    for elemento in fila: # En cada iteracion recoge un valor de fila, es decir, un elemento, 1 en la primera iteracion, por ejemplo
        print(elemento, end=" ") # Imprime el elemento, end=" " es para que no salte de linea sino que ponga un espacio entre los elementos de la fila
    print() # Salta de linea, es decir, pasa a la siguiente fila
print("\n")
# Aunque no hemos visto, aun, el bucle for, lo usamos a modo de ejemplo de como imprimir una matriz rapidamente, podemos hacerlo sin for
print("Representacion de una matriz con una lista de listas sin bucle for")
print(*lista_de_listas, sep="\n") 
# *lista_de_listas es para desempaquetar la lista, es decir, imprimir cada elemento de la lista en una linea diferente, sep="\n" es para que salte de linea
print("\n")

# Otro modo es acceder con los indices a la posicion de cada elemento
print("Representacion de una matriz con una lista de listas accediendo con indices")
print(lista_de_listas[0]) # Imprimimos el primer elemento de la lista de listas, es decir, la primera fila, los indices empiezan en 0 en Python por convencion  
print(lista_de_listas[1]) # Imprimimos el segundo elemento de la lista de listas, es decir, la segunda fila
print(lista_de_listas[2]) # Imprimimos el tercer elemento de la lista de listas, es decir, la tercera fila

# Veamos distintos modos de acceder a los elementos de una lista con los indices
frutas = ["Manzana", "Banana", "Mango", "Piña", "Uva", "Melon", "Pera"]
# Accedemos al primer elemento de la lista con el indice 0
print(f"El primer elemento de la lista de frutas es: {frutas[0]}")
# Accedemos al segundo elemento de la lista con el indice 1, esto es, como por convencion los indices empiezan en 0 el segundo elemento es el indice 1
print(f"El segundo elemento de la lista de frutas es: {frutas[1]}")

# En Python podemos acceder a los elementos de una lista de forma inversa con indices negativos, en este caso no empezariamos en 0 ya que colisionaria con el indice 0
# El primer elemento en una lista de forma inversa es el ultimo elemento, es decir, el indice -1
print(f"El ultimo elemento de la lista de frutas es: {frutas[-1]}")
print(f"El penultimo elemento de la lista de frutas es: {frutas[-2]}")

# Como funciona esto de los indices e indices negativos en una lista de listas o matriz, debemos usar un indice para acceder a la fila 
# y otro para acceder a los elementos de la fila, lo que vendria a ser la columna.
matriz = [[1,3,5],[2,4,6],[3,7,11]]
# Pintemos la matriz para ver luego el acceso a los elementos de modo mas sencillo
print(matriz[0])
print(matriz[1])
print(matriz[2])

# Accedemos a los elementos de la matriz con su fila y columna.
print(f"El primer elemento de la primera fila de una lista de listas, o matriz, es: {matriz[0][0]}") # Devuelve 1
print(f"El segundo elemento de la primera fila de una lista de listas, o matriz, es: {matriz[0][1]}") # Devuelve 3
print(f"El tercer elemento de la primera fila de una lista de listas, o matriz, es: {matriz[0][2]}") # Devuelve 5
# Como en el caso anterior podemos usar indices negativos, tanto para filas, como para columnas
print(f"El ultimo elemento de la primera fila de una lista de listas, o matriz, es: {matriz[0][-1]}") # Devuelve 5
print(f"El primer elemento de la ultima fila de una lista de listas, o matriz, es: {matriz[-1][0]}") # Devuelve 3
print(f"El ultimo elemento de la ultima fila de una lista de listas, o matriz, es: {matriz[-1][-1]}") # Devuelve 11

# Slicing, o rebanado, es una forma de acceder a una porcion de una lista
# El formato completo de un slice es [inicio:fin:paso]
# inicio es el indice inicial, sino esta presente se entiende como 0
# fin es el indice final, sino esta presente se entiende como el ultimo elemento de la lista
# paso es el numero de elementos a saltar en cada iteracion, sino esta presente se entiende como 1
print("\n")
print("Recordemos la lista de frutas de las que queremos hacer slice:")
print(frutas)
print("Slice de la lista de frutas con inicio en el indice 1, posición 2, fin en el indice 4, posición 5")
print("Devuelve las frutas desde la posición 2 hasta la posición 5, pero la posición 5 no se incluye") 
print(frutas[1:4]) # Devuelve "Banana", "Mango", "Piña"
# Añadimos el paso y lo hacemos con indices negativos, empezamos en el ultimo elemento y terminamos en el cuarto elemento por el final, vamos saltando de 2 en 2 con -2
print("\n")
print("Slice de la lista de frutas con inicio en el indice -1, posición 7, fin en el indice -4, posición 4, paso -2")
print("Devuelve las frutas desde la posición 7 hasta la posición 4, pero la posición 4 no se incluye")
print("Como vemos, el paso es negativo, por lo que recorre la lista de forma inversa, y lo hacemos con saltos de 2 posiciones")
print(frutas[-1:-4:-2]) # Devuelve "Pera", "Uva"

# Slice con valores implicitos
print("\n")
print("Slice con valores implicitos")
print("Devuelve las frutas desde la posición 0 hasta la posición 5, pero la posición 5 no se incluye")
print(f"frutas[:5] = {frutas[:5]}") # Devuelve "Manzana", "Banana", "Mango", "Piña", "Uva"
print("Devuelve las frutas desde la posición 2 hasta la posición final")
print(f"frutas[2:] = {frutas[2:]}") # Devuelve "Mango", "Piña", "Uva", "Melon", "Pera"
print("Devuelve las frutas desde la posición inicial hasta la posición final")
print(f"frutas[:] = {frutas[:]}") # Devuelve "Manzana", "Banana", "Mango", "Piña", "Uva", "Melon", "Pera"
print("Devuelve las frutas desde la posición final hasta la posición inicial en orden inverso ya que el paso es negativo")
print(f"frutas[::-1] = {frutas[::-1]}") # Devuelve "Pera", "Melon", "Uva", "Piña", "Mango", "Banana", "Manzana"

# Podemos usar los slices para hacer una copia de una lista
lista1 = [1,2,3,4,5]
lista2 = lista1[:]
print("\n")
print("Hacemos una copia de una lista en otra variable con el slice [:]")
print("Lista 1:", lista1)
print("Lista 2 creada con la lista 1 y el slice [:]:", lista2)
# La verdadera potencia de estas creaciones viene de crear listas modificadas de la lista original, por ejemplo, invertimos el orden de los elementos de la lista original
lista2 = lista1[::-1]
print("Lista 2 creada con la lista 1 y el slice [::-1]:", lista2)
# Sabemos que la lista esta ordenada de menor a mayor, por lo que podemos usar el slice para obtener los elementos pares e impares
# Solo queremos los elementos pares de la lista original
lista2 = lista1[1::2]
print("Lista 2 creada con la lista 1 y el slice [1::2]:", lista2)
# Solo queremos los elementos impares de la lista original
lista2 = lista1[::2]
print("Lista 2 creada con la lista 1 y el slice [::2]:", lista2)


# Determinar el numero de elementos de una lista mediante la funcion len()
print("\n")
print(f"El numero de elementos de la lista de frutas es: {len(frutas)}")

### METODOS DEL OBJETO LISTA ###

# Podemos hacer una copia de una lista ordenada con el metodo copy()
lista = ["pepe", "juan", "luis", "ana", "maria"]
print("Lista original:", lista)
copia_lista = lista.copy()
print("Copia de la lista con el metodo copy():", copia_lista)


# Modificaciones de una lista, lo hacemos mediante metodos que van incorporados al objeto lista.
lista = ["pepe", "juan", "luis", "ana", "maria"]
print("Lista original:", lista)

# Añadir elementos con metodos
# append() añade un elemento al final de la lista
lista.append("jorge")
print("Añadimos a la lista el elemento 'jorge' con la funcion append(), el elemento se añade al final de la lista:", lista)
# Añadimos un elemento en una posicion determinada mediante el metodo insert(), insert lleva dos parametros, el indice donde insertamos el elemento y el elemento a insertar
lista.insert(3, "sisebuto")
print("Lista con el elemento 'sisebuto' insertado en la posicion 3 con la funcion insert():", lista)
# Añadimos varios elementos, al final de la lista, con el metodo extend(), extend lleva un parametro.
lista.extend(["genaro", "javier", "eva", "alicia"])
print("Lista con los elementos 'genaro', 'javier', 'eva' y 'alicia' añadidos con la funcion extend():", lista)

# Eliminar elementos con metodos
# remove() elimina el elemento pasado como parametro de la lista, SOLO la primera aparicion del elemento, si hay mas no se eliminan
lista.remove("pepe")
print("Eliminamos de la lista el elemento 'pepe' con la funcion remove():", lista)
# pop() elimina el ultimo elemento de la lista
lista.pop() # Elimina el ultimo elemento de la lista, en este caso "Jorge"
print("Lista con el ultimo elemento eliminado con la funcion pop():", lista)
# pop() si le pasamos un parametro, elimina el elemento en el indice pasado como parametro, podemos pasar indices negativos
lista.pop(2)
print("Lista con el elemento en el indice 2, posicion 3, eliminado con la funcion pop():", lista)

# sort() ordena la lista
# El metodo sort no devuelve nada, es decir, no devuelve la lista ordenada, sino que ordena la lista original machacando lo que habia antes
# esto es importante porque no podemos darle el resultado de la funcion sort() a una variable. No podemos hacer lista_ordenada = lista.sort()
# debemos hacer lista.sort() y luego lista_ordenada = lista
lista.sort() 
print("Lista ordenada con la funcion sort():", lista)
# reverse() ordena la lista en orden inverso
lista.reverse()
print("Lista ordenada en orden inverso con la funcion reverse():", lista)
# clear() vacia la lista
lista.clear()
print("Lista vacia con la funcion clear():", lista)
print("\n")

# Metodo de una lista para pasar todos sus elementos a minusculas, los elementos deben ser del tipo cadena de caracteres
lista = ["Pepe", "Juan", "Luis", "Ana", "Maria"]
# lower() pasa todos los elementos a minusculas
lista = ["Pepe".lower(), "Juan".lower(), "Luis".lower(), "Ana".lower(), "Maria".lower()] # Podriamos hacerlo con un for, pero aun no hemos llegado ahi.
print("Lista con todos los elementos en minusculas con la funcion lower():", lista)
# upper() pasa todos los elementos a mayusculas
lista = ["Pepe".upper(), "Juan".upper(), "Luis".upper(), "Ana".upper(), "Maria".upper()] # Podriamos hacerlo con un for, pero aun no hemos llegado ahi.
print("Lista con todos los elementos en mayusculas con la funcion upper():", lista)
print("\n")

# lower, o upper, pueden ser usados como clave del metodo sort()
lista = ["Pepe", "juan", "Luis", "ana", "Maria"]
lista.sort()
print("Lista ordenada con la funcion sort(), vemos que ordena primero por mayusculas y luego por minusculas:", lista)
lista.sort(key=str.lower)
print("Lista ordenada con la funcion sort(key=str.lower), ordenadas con independencia de si comienza por mayuscula o minuscula:", lista)
lista.sort(key=str.upper)
print("Lista ordenada con la funcion sort(key=str.upper), ordenadas con independencia de si comienza por mayuscula o minuscula:", lista)
print("\n")

# Contar las veces que aparece un elemento en una lista con el metodo count()
lista = ["pepe", "juan", "luis", "ana", "maria", "pepe", "juan", "luis", "ana", "maria", "pepe"]
print("Lista original:", lista)
print("El elemento 'pepe' aparece", lista.count("pepe"), "veces")
print("El elemento 'juan' aparece", lista.count("juan"), "veces")
print("El elemento 'luis' aparece", lista.count("luis"), "veces")
print("El elemento 'ana' aparece", lista.count("ana"), "veces")
print("El elemento 'maria' aparece", lista.count("maria"), "veces")
print("\n")

# Podemos determinar si un elemento esta en una lista mediante la palabra reservada in
lista = ["pepe", "juan", "luis", "ana", "maria"]
print("pepe" in lista)
print("juan" in lista)
print("ana" in lista)
print("genaro" in lista)
print("\n")

### FIN METODOS DEL OBJETO LISTA ###

# Existe una funcion para borrar elementos de una lista, es del tipo del operador del
# del() elimina el elemento en el indice pasado como parametro, podemos pasar indices negativos
lista = ["pepe", "juan", "luis", "ana", "maria"]
print("Lista original:", lista)
del lista[2]
print("Lista con el elemento en el indice 2, posicion 3, eliminado con la funcion del():", lista)
# Podemos pasarle un rango de indices para eliminar varios elementos, mediante un slice
lista = ["pepe", "juan", "luis", "ana", "maria"]
del lista[1:3] # Elimina los elementos en el rango de indices 1 a 3, posiciones 2 y 3, "juan" y "luis"
print("Lista con los elementos en el rango de indices 1 a 3, posiciones 2 y 3, eliminados con la funcion del():", lista)
# Podemos eliminar todos los elementos de la lista con la funcion del() y el slice [:]
lista = ["pepe", "juan", "luis", "ana", "maria"]
del lista[:]
print("Lista con todos los elementos eliminados con la funcion del() y el slice [:]:", lista)
print("\n")

# Podemos ordenar una lista con la funcion sorted(), a diferencia del metodo sort(), sorted() si devuelve la lista ordenada y podemos asignarla a una variable
lista_desordenada = [3,1,4,1,5,9,2,6,5,3,5]
lista_ordenada = sorted(lista_desordenada)
print("\n")
print("Usamos la funcion sorted() para ordenar la lista desordenada")
print("Lista desordenada:", lista_desordenada)
print("Lista ordenada:", lista_ordenada)


# Modificaciones de una lista con el indice
lista = ["pepe", "juan", "luis", "ana", "maria"]
lista[2] = "jorge"
print("Lista con el elemento en el indice 2, posicion 3, modificado, cambiando su valor por 'jorge', modificacion directa con el indice:", lista)
# Podemos concatenar listas, o elementos, con el operador +
lista = ["pepe", "juan", "luis", "ana", "maria"]
lista2 = ["jorge", "lucas", "alicia", "marcos"]
lista3 = lista + lista2
print("Lista 1:", lista)
print("Lista 2:", lista2)
print("Lista con la lista 2 concatenada con la lista 1 con el operador +:", lista3)
print("\n")

# Si queremos añadir elementos a una lista podemos usar el operador += en vez de la concatenacion de listas
# Esta forma es mas eficiente ya que no crea una nueva lista y nos ahorra espacio en memoria
print("Lista original:", lista)
lista += ["jorge", "lucas"]
print("Lista con los elementos 'jorge' y 'lucas' añadidos con el operador +=:", lista)



