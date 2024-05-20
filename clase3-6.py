archivo_nombre= "hola.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_liata=archivo.readlines()   # se crea la lista del archivo gpi.txt 
    
num_linea=1
lin_tol= len(lineas_liata)
linea_tol_vasia=0
linea_tol_texto=0


for linea in lineas_liata:  # separa la lista por lineas "linea"
    
    if linea.strip() == "":  # elimina las lineas vacias de la lista  
            print("lineas vacias ")   
            linea_tol_vasia=linea_tol_vasia+1  # cuantas lineas hay vasias y incrementa en 1 cunado lo encuentra 
            continue
    print("linea", num_linea," : ",linea)
    num_linea=num_linea+1
    
    linea_tol_texto=lin_tol-linea_tol_vasia  # dice la slineas d etexto  que hay
    
print("las lineas totales son: ",lin_tol)
print("lineas vacias: ",linea_tol_vasia)
print ("liena con texto:",linea_tol_texto)
    
