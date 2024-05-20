import os
carpeta="documentos\\"
archivo="gpi.txt"


with open(carpeta+archivo,"r") as archivo:
     texto=archivo.read()
     
simbolos=["(",")",",",".",";",":","/"] #lista de simbolos

for simbolos in simbolos:
    texto=texto.replace(simbolos," " + simbolos + " ") #reemplazar simbolos por simbolos con espacios
    
palabras_lista=texto.split() #separar palabras .split() sirve para separar palabras 
palabras_lista.sort() #ordenar palabras .sort() sirve para ordenar listas
for palabra in  palabras_lista: #imprimir palabras ordenadas
    print(palabra)     