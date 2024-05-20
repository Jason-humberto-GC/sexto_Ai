archivo_nombre= "gpi.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_liata=archivo.readlines()  # readlines lo mete todo en una lista y lo pone jjunto
print(lineas_liata)