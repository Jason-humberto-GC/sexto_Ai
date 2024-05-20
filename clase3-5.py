archivo_nombre= "hola.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_liata=archivo.readlines()   # se crea la lista del archivo gpi.txt 
    
num_linea=1
lineas_H=0
lineas_v=0

for linea in lineas_liata:  # separa la lista por lineas "linea"
    
    if linea.strip() == "":  # elimina las lineas vacias de la lista  
            continue
    print("linea", num_linea," : ",linea)
    num_linea=num_linea+1


