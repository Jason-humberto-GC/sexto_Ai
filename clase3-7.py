import os
carpeta_nombre ="documentos\\"
archivo_lista=os.listdir(carpeta_nombre) # lista los archivos de la carpeta documentos  
for archivo_nombre in archivo_lista:
    print(archivo_nombre) 