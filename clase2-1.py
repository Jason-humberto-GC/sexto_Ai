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


s3=open(c+s,"r")
print(s3.read()) #le el archivo nuevo  s2 "clase2-2"
s3.close()
