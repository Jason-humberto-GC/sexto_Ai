carpeta_nombre="documentos\\" 
archivo_nombre="gpi.txt"

print("lectura del archivo: \n",open(carpeta_nombre+archivo_nombre,"r").read())  #.read() sirve para leer archivos

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read() 
palabras_lista=texto.split() #separar palabras .split() sirve para separar palabras
print("palabras separadas: \n",palabras_lista) #imprimir palabras separadas
palabras_lista.sort()  #ordenar palabras .sort() sirve para ordenar listas
print("palabras ordenadas: \n")
for palabra in palabras_lista: 
    print(palabra)   #imprimir palabras ordenadas
    