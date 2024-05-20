archivo_nombre= "gpi.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_liata=archivo.readlines()   # separa la lista por lineas
#print(lineas_liata)
for linea in lineas_liata:
    print(linea)