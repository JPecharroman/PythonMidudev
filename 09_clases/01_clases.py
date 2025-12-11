# Clases en Python

# Ref: https://docs.python.org/3/tutorial/classes.html

# Hemos visto al crear la conexion con la API de OpenAI y la de Deepseek, que sus programas son muy similares, deberiamos poder encapsular esta logica en una clase 
# para poder reutilizarla.

# Creamos una clase llamada API
# Las clases en Python son como plantillas para crear objetos, es decir, podemos crear varios objetos a partir de una clase.
# En este caso, la clase API es una plantilla para crear objetos que puedan llamar APIs que sigan el patron de OpenAI.
# Como hemos visto en el caso anterior, aqui podriamos crear un objeto de la clase API para llamar a la API de OpenAI y otro para llamar a la API de Deepseek.

# Las clases nos permiten agrupar datos y funciones(metodos) que son comunes a todos los objetos que creemos a partir de la clase.
"""
Ejemplo tipo de clase:

class Persona:
    # Funciones, metodos, comunes a todas las instancias de la clase
    # Constructor, __init__ es un metodo especial que se ejecuta al crear un objeto, se llama automaticamente al crear un objeto
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
    
    def modificar_genero(self, genero):
        self.genero = genero # Modificamos el atributo genero accediendo a el con self

    # Atributos de la clase, comunes a todas las instancias de la clase
    raza = "Humano"
    genero = "Masculino"

# Creamos un objeto de la clase Persona
persona1 = Persona("Jorge", "Fernandez", 30)
persona1.presentarse()

# Creamos otro objeto de la clase Persona
persona2 = Persona("Ana", "Garcia", 25) # Hemos creado esta instancia de la clase Persona, podemos acceder a sus atributos y metodos, vamos a cambiar el genero de Ana
persona2.modificar_genero("Femenino")
persona2.presentarse()

# Accedemos al atributo raza de la clase Persona
print(persona1.raza)
print(persona2.raza)

"""

# Encapsulamos la logica de la API en una clase, la encapsulacion es una caracteristica de la programacion orientada a objetos que nos permite ocultar los 
# detalles de la implementacion de una clase y exponer solo los metodos y atributos que sean necesarios para que el usuario pueda usar la clase.

class openai_api:

    # Creamos un constructor que recibe la API key y la url de la API como parametro
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.base_url = url

    def llamar_api(self, model, messages):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        body = {
            "model": model,
            "messages": messages
        }
        response = requests.post(self.base_url, headers=headers, json=body)
        return response.json()

# Creamos un objeto de la clase openai_api para acceder a la API de OpenAI
api_key_openai = "Aqui iria la API key de OpenAI"
url_openai = "https://api.openai.com/v1/chat/completions"
clase_openai = openai_api(api_key_openai, url_openai)
# Ahora, podemos llamar a la API de OpenAI, necesitamos, para llamar a la api pasarle el modelo y los mensajes
modelo = "gpt-3.5-turbo"
mensajes = [
    {
        "role": "user",
        "content": "Escribe un poema breve sobre la vida"
    }
]

# Llamamos a la API de OpenAI
respuesta_json = clase_openai.llamar_api(modelo, mensajes)
print(json.dumps(respuesta_json, indent=4))
print(respuesta_json["choices"][0]["message"]["content"])

# Creamos un objeto de la clase openai_api para acceder a la API de Deepseek
api_key_deepseek = "Aqui iria la API key de Deepseek"
url_deepseek = "https://api.deepseek.com/chat/completions"
clase_deepseek = openai_api(api_key_deepseek, url_deepseek)
# Ahora, podemos llamar a la API de Deepseek, necesitamos, para llamar a la api pasarle el modelo y los mensajes
modelo = "deepseek-chat"
# El mensaje es el mismo asi que reusamos el anterior.

# Llamamos a la API de Deepseek
respuesta_json = clase_deepseek.llamar_api(modelo, mensajes)
print(json.dumps(respuesta_json, indent=4))
print(respuesta_json["choices"][0]["message"]["content"])