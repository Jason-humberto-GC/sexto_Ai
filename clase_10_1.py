import PyPDF2
import docx
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import matplotlib.pyplot as plt

def extraer_texto_pdf(pdf_path):
    texto_extraido = ""
    with open(pdf_path, "rb") as archivo_pdf:
        lector_pdf = PyPDF2.PdfReader(archivo_pdf)
        num_paginas = len(lector_pdf.pages)
        for pagina_numero in range(num_paginas):
            pagina = lector_pdf.pages[pagina_numero]
            texto_extraido += pagina.extract_text()
    return texto_extraido

def extraer_texto_docx(docx_path):
    texto_pagina = ""
    documento = docx.Document(docx_path)
    for parrafo in documento.paragraphs:
        texto_pagina += parrafo.text + "\n"
    return texto_pagina

def contar_palabras_lineas(texto):
    palabras = texto.split()
    lineas = texto.split('\n')
    return len(palabras), len(lineas)

def contar_frecuencia_palabra(texto, palabra):
    palabras = word_tokenize(texto.lower())
    return palabras.count(palabra.lower())

def contar_palabras_cortas(texto):
    palabras_cortas = [palabra for palabra in texto.split() if len(palabra) in [3, 4]]
    return palabras_cortas

def guardar_texto_archivo(texto, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

if __name__ == "__main__":
    tipo_archivo = input("¿El archivo es un PDF (P) o un documento DOCX (D)?: ").upper()
    if tipo_archivo == "P":
        pdf_nombre = input("Por favor, ingrese el nombre del archivo PDF (sin la extensión .pdf): ")
        pdf_path = pdf_nombre + (".pdf" if not pdf_nombre.endswith(".pdf") else "")
        texto_extraido = extraer_texto_pdf(pdf_path)
    elif tipo_archivo == "D":
        docx_nombre = input("Por favor, ingresa el nombre del archivo .docx (incluyendo la extensión): ")
        texto_extraido = extraer_texto_docx(docx_nombre)
    else:
        print("Tipo de archivo no válido.")
        exit()

    # Continuar con el resto del código utilizando el texto extraído
    num_palabras, num_lineas = contar_palabras_lineas(texto_extraido)
    print("----------------------------------------------------------------------")
    print("Número de palabras en el documento:", num_palabras)
    print("Número de líneas de texto en el documento:", num_lineas)

    palabra_a_buscar = input("Ingrese la palabra que desea buscar en el documento: ")
    frecuencia_palabra = contar_frecuencia_palabra(texto_extraido, palabra_a_buscar)
    print("----------------------------------------------------------------------")
    print(f"La palabra '{palabra_a_buscar}' aparece {frecuencia_palabra} veces en el documento.")

    palabras_cortas = contar_palabras_cortas(texto_extraido)
    print("----------------------------------------------------------------------")
    print("Palabras cortas de 3 o 4 caracteres:", palabras_cortas)

    # Guardar el texto extraído en un archivo de texto
    if texto_extraido:
        guardar_texto_archivo(texto_extraido, "texto_pagina.txt")

    # Cargar palabras funcionales en español de NLTK
    nltk.download("stopwords")
    nltk.download("punkt")
    palabras_funcionales = stopwords.words("spanish")
    for palabra_funcional in palabras_funcionales:
        print(palabra_funcional)

    print("----------------------------------------------------------------------")

    # Tokenizar el texto y eliminar palabras funcionales
    tokens = word_tokenize(texto_extraido, "spanish")
    tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

    print("tokens limpios")
    print(tokens_limpios)
    print("----------------------------------------------------------------------")
    print("Número total de tokens:", len(tokens))
    print("----------------------------------------------------------------------")
    print("Número de tokens limpios:", len(tokens_limpios))

    # Crear un objeto Text de NLTK y calcular la distribución de frecuencia
    texto_limpio_nltk = nltk.Text(tokens_limpios)
    distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

    # Graficar las 40 palabras más comunes
    distribucion_limpia.plot(40)
