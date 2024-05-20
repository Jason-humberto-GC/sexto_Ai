#crear un nuevo archivo  y copiar lo que esta en el acrchivo gpi


c="C:\\Users\\jason\\Downloads\\sexto\\sexto iA\\"
e="gpi.txt"
s="clase2-2.txt"

e2=open(c+e,"r")
#print(e2.read())  ##lee el archivo gpi y lo imprime 

s2=open(c+s,"w")
t=e2.read()
t2=t
s2.write(t2) ## realiza el copiado del archivo s2 en t2

e2.close()
s2.close()

with open(c+s,"r") as archivo:      #forma dos de abrir un archivo 
    texto=archivo.read()
print(texto)

