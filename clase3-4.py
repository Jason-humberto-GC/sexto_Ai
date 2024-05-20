archivo_nombre= "gpi.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_liata=archivo.readlines()   # se crea la lista del archivo gpi.txt 
    
num_linea=1

for linea in lineas_liata:  # separa la lista por lineas "linea"
    print("numero de lineas: ",num_linea ," : ", linea)   #  # separa la lista por lineas y ponerles el nuero de linea que son  apartir del  espacio 1 asignado en num_linea
    num_linea=num_linea+1