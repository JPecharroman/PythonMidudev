# Tratamiento de fechas y horas en Python

# importamos funciones del modulo datetime, no lo importamos todo, solo las que necesitemos, economia de memoria
from datetime import datetime, timedelta
from os import system

# Vamos a importar otra funcion de otro modulo, del modulo locale traemos la funcion setlocale, para cambiar el formato de la fecha a español
# LC_TIME es una constante que indica que queremos cambiar el formato de la fecha, debemos importarla tambien
from locale import setlocale, LC_TIME
# Ponemos el formato de la fecha a español
setlocale(LC_TIME, 'es_ES.UTF-8')

system("cls")

# Creamos una fecha y hora con el metodo now()
fecha = datetime.now()
print(f"Fecha en formato anglosajon: {fecha}")

# Formateamos la fecha con el metodo strftime()
# %d dia
# %m mes
# %Y año
# %H hora
# %M minutos
# %S segundos
# A la fecha almacenada en la variable fecha le aplicamos el metodo strftime() para formatearla con los parametros indicados
fecha_formateada = fecha.strftime("%d-%m-%Y %H:%M:%S")
print(f"Fecha formateada a formato europeo: {fecha_formateada}")
# Podemos poner el dia de la semana
fecha_formateada = fecha.strftime("%A %d-%m-%Y %H:%M:%S")
print(f"Fecha formateada a formato europeo: {fecha_formateada}")
fecha_formateada = fecha.strftime("%A, %d de %B de %Y %H:%M:%S")
print(f"Fecha formateada con mes en letra: {fecha_formateada}")

# Hallamos el dia de la semana
fecha_actual = datetime.now()
dia_semana = fecha_actual.strftime('%A')
print(f"Dia de la semana: {dia_semana}")

# Fecha, y hora, especifica
fecha_especifica = datetime(2022, 5, 6, 12, 30, 0)
print(f"Fecha especifica: {fecha_especifica}")
fecha_formateada = fecha_especifica.strftime("%d-%m-%Y %H:%M:%S")
print(f"Fecha especifica formateada a formato europeo: {fecha_formateada}")

# Creamos una fecha y hora con el metodo strptime()
fecha2 = datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
print(f"Fecha formateada a formato europeo: {fecha2}")


# Operaciones con fechas
fecha1 = datetime(2022, 5, 8, 14, 45, 0)
fecha2 = datetime(2022, 5, 6, 12, 30, 0)
diferencia = fecha1 - fecha2
print(f"Diferencia entre las fechas: {diferencia}")


# Hallar fechas a partir de la fecha actual
# Hallamos el dia de ayer
fecha_actual = datetime.now()
fecha_ayer = fecha_actual - timedelta(days=1) # Restamos un dia a la fecha actual con la funcion timedelta()
print(f"Fecha de ayer: {fecha_ayer.strftime('%d-%m-%Y')}")

# Hallamos el dia de mañana
fecha_manana = fecha_actual + timedelta(days=1) # Sumamos un dia a la fecha actual con la funcion timedelta()
print(f"Fecha de mañana: {fecha_manana.strftime('%d-%m-%Y')}")

# A timedelta le podemos pasar varios parametros dias, horas, minutos y segundos...
# No funciona con meses y años
fecha2 = fecha_actual + timedelta(days=1, hours=12, minutes=30, seconds=0)
print(f"Fecha random: {fecha2.strftime('%d-%m-%Y %H:%M:%S')}")


# Recuperar componentes de una fecha
fecha_actual = datetime.now()
dia = fecha_actual.day
mes = fecha_actual.month
anio = fecha_actual.year
print(f"Dia: {dia}, Mes: {mes}, Año: {anio}")