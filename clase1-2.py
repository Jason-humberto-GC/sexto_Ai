###escritura de un archivo que ya existe, en donde se modifica lo que tiene y se ponen nuevos datos desde el codigo 
archivo_abierto=open("C:\\Users\\jason\\Downloads\\sexto\\sexto iA\\gpi.txt","w")

archivo_abierto.write("Esto es escribe en el archivo\n")
archivo_abierto.write("Esto tambien\n")
archivo_abierto.write("mira, puedo escribir \"comillas\" \n")
archivo_abierto.write("gracias a la diagonal invertida:  \n")
archivo_abierto.close()

## ver lo que se modifico en el archivo de texto 
archivo_abierto=open("C:\\Users\\jason\\Downloads\\sexto\\sexto iA\\gpi.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()