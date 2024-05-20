import openai
from openai import OpenAI

client = OpenAI(
  organization='org-dhhGVG0aW4eza6VEyBdS9CQv',
  project='$PROJECT_ID',
)
# Función para registrar consultas y respuestas
def registrar(consulta, respuesta):
  with open("log.txt", "a") as archivo:
    archivo.write(f"Consulta: {consulta}\nRespuesta: {respuesta}\n\n")

# Función para enviar una solicitud de chat a ChatGPT
def enviar_solicitud_chat(mensaje):
  try:
    respuesta = openai.Completion.create(
      engine='text-davinci-003',
      prompt=mensaje,
      max_tokens=50,
      temperature=0.7
    )
    respuesta_texto = respuesta.choices[0].text.strip()
    registrar(mensaje, respuesta_texto)
    return respuesta_texto
  except Exception as e:
    error = f"Ocurrió un error al enviar la solicitud de chat: {str(e)}"
    registrar(mensaje, error)
    return error

# Función para interactuar con el usuario
def interactuar():
  print("¡Bienvenido al ChatGPT!")
  print("Puedes comenzar a escribir tus mensajes. Escribe 'salir' para terminar la conversación.")
  print("-----------------------------------------")

  # Loop de interacción
  while True:
    mensaje = input("Usuario: ")

    if mensaje.lower() == 'salir':
      break

    respuesta = enviar_solicitud_chat(mensaje)
    print("ChatGPT:", respuesta)
    print("-----------------------------------------")

# Ejecutar la función de interacción
interactuar()
