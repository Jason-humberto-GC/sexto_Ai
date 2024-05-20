import re #importar el modulo de expresiones regulares
carpeta="documentos\\"
archivo="hola.txt"
cont=0
with open (carpeta+archivo,"r") as  archivo:
    texto=archivo.read()
    
expresion_regular=re.compile(r"apellid[o][os]?") #compilar la expresion regular la funcion compile() sirve para compilar la expresion regular

resultado_busqueda=expresion_regular.finditer(texto) #finditer sirve para buscar todas las coincidencias de la expresion regular en el texto
for resultado in resultado_busqueda:
    print(resultado.group(0))
