##conseptos basicos
print("primera parte de la clase\n")
print("universidad de colima")
print("ingenieria en computacion inteligente")
nombre="jason humberto garcia camacho"
print("hola", nombre)
edad= input("escribe tu edad: ")
print(nombre, "tiene la edad de: ",edad, " años")
print("operacion1", 4*5-6)
x=4+7
y=x-2
z=x+y
print("x: ", x)
print("y: ", y)
print("z: ", z, "\n")

print("segunda parte de la clase \n ")
##abrir un archivo de texto sin modificarlos y visualisarlo en la terminal 
archivo_abierto=open("C:\\Users\\jason\\Downloads\\sexto iA\\hola.txt")
texto=archivo_abierto.read()
print(texto,"\n")
archivo_abierto.close()

print("tercera parte de la clase \n")
###escritura de un archivo que ya existe, en donde se modifica lo que tiene y se ponen nuevos datos desde el codigo 
archivo_abierto=open("C:\\Users\\jason\\Downloads\\sexto iA\\gpi.txt","w")

archivo_abierto.write("Esto es escribe en el archivo\n")
archivo_abierto.write("Esto tambien\n")
archivo_abierto.write("mira, puedo escribir \"comillas\" \n")
archivo_abierto.write("gracias a la diagonal invertida:  \n")
archivo_abierto.close()

## ver lo que se modifico en el archivo de texto 
archivo_abierto=open("C:\\Users\\jason\\Downloads\\sexto iA\\gpi.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()