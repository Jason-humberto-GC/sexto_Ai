import requests
import nltk
from bs4 import BeautifulSoup

# Función para contar palabras de 3 o 4 caracteres
def contar_palabras_cortas(texto):
    palabras_cortas = [palabra for palabra in texto.split() if len(palabra) in [3, 4]]
    return palabras_cortas

# Función para contar el número de veces que aparece una palabra fija en el texto
def contar_palabra_fija(texto, palabra_fija):
    return texto.lower().count(palabra_fija.lower())

# Obtener el texto de una página web
def obtener_texto_pagina(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texto_pagina = soup.get_text()
    return texto_pagina

# Guardar el texto extraído en un archivo de texto
def guardar_texto(texto, archivo_nombre):
    with open(archivo_nombre, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

# Cargar el texto del archivo
def cargar_texto(archivo_nombre):
    with open(archivo_nombre, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    return texto

# URL de la página web
url_pagina = input("Introduce la URL de la página web: ")

# Obtener el texto de la página web
texto_pagina = obtener_texto_pagina(url_pagina)

# Guardar el texto en un archivo
guardar_texto(texto_pagina, "texto_pagina.txt")

# Contar el número de palabras
num_palabras = len(texto_pagina.split())

# Contar el número de líneas
num_lineas = len(texto_pagina.splitlines())

# Mostrar palabras de 3 o 4 caracteres
palabras_cortas = contar_palabras_cortas(texto_pagina)

# Contar el número de veces que aparece una palabra fija en el texto
print("----------------------------------------------------------------------")
palabra_fija = input("Introduce la palabra fija que deseas buscar: ")
num_veces_palabra_fija = contar_palabra_fija(texto_pagina, palabra_fija)

# Imprimir resultados
print("----------------------------------------------------------------------")
print("Número de palabras en la página:", num_palabras)
print("----------------------------------------------------------------------")
print("Número de líneas de texto en la página:", num_lineas)
print("----------------------------------------------------------------------")
print("Palabras de 3 o 4 caracteres:", palabras_cortas)
print("----------------------------------------------------------------------")
print(f"La palabra '{palabra_fija}' aparece {num_veces_palabra_fija} veces en el texto.")
print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
nltk.download('stopwords')
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
print("----------------------------------------------------------------------")
print("Palabras funcionales en español:")
print(palabras_funcionales)
print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto_pagina, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)
