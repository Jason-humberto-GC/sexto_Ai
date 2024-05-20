#if  busqueda de una palabra
#ruta y nombre del archivo 
c="C:\\Users\\jason\\Downloads\\sexto\\sexto iA\\"
e="hola.txt"
#palabra="apellido"   busqueda de una sola palabra 
palabra=input("ingresa la palabra a buscar: ")  #busqueda de una palabra buscada por el usuario 
palabra1=palabra.lower()
with open(c+e,"r") as archivo:      #forma dos de abrir un archivo 
    texto=archivo.read()
#print(texto)  

if palabra1 in texto:
    print("palabra en contrada")
else:
    print("no encontre l apalabra ")
